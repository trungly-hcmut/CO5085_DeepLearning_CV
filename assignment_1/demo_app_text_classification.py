import streamlit as st
import torch
import torch.nn as nn
import json
import os
import re
from torch.nn.utils.rnn import pack_padded_sequence

# ===== Load configuration =====
MODELS_DIR = 'saved_models'
MAX_LEN = 80
PAD_ID = 0
UNK_ID = 1

# Device
device = torch.device('mps' if torch.backends.mps.is_available() else ('cuda' if torch.cuda.is_available() else 'cpu'))

# ===== Define Models =====
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes, dropout=0.3):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=PAD_ID)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim * 2, num_classes)

    def forward(self, x):
        emb = self.embedding(x)
        lengths = (x != PAD_ID).sum(dim=1).cpu()
        lengths = torch.clamp(lengths, min=1)
        packed = pack_padded_sequence(emb, lengths, batch_first=True, enforce_sorted=False)
        _, (h_n, _) = self.lstm(packed)
        h = torch.cat([h_n[-2], h_n[-1]], dim=1)
        h = self.dropout(h)
        return self.fc(h)


class TransformerClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads, ff_dim, num_layers, num_classes, max_len=MAX_LEN, dropout=0.2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=PAD_ID)
        self.pos_embedding = nn.Embedding(max_len, embed_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=ff_dim,
            dropout=dropout,
            batch_first=True,
            activation='gelu'
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers, enable_nested_tensor=False)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        bsz, seq_len = x.size()
        pos_ids = torch.arange(seq_len, device=x.device).unsqueeze(0).expand(bsz, seq_len)
        emb = self.embedding(x) + self.pos_embedding(pos_ids)
        key_padding_mask = (x == PAD_ID)
        enc = self.encoder(emb, src_key_padding_mask=key_padding_mask)
        mask = (x != PAD_ID).unsqueeze(-1).float()
        pooled = (enc * mask).sum(dim=1) / torch.clamp(mask.sum(dim=1), min=1.0)
        pooled = self.dropout(pooled)
        return self.fc(pooled)


# ===== Load vocabulary =====
@st.cache_resource
def load_vocab():
    vocab_path = os.path.join(MODELS_DIR, 'vocab_metadata.json')
    with open(vocab_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    word2id = metadata['word2id']
    id2label = {int(k): v for k, v in metadata['id2label'].items()}
    category_names = metadata['category_names']
    vocab_size = metadata['vocab_size']
    
    return word2id, id2label, category_names, vocab_size


# ===== Load models =====
@st.cache_resource
def load_models(vocab_size, num_classes):
    models = {}
    
    # LSTM
    lstm_model = LSTMClassifier(
        vocab_size=vocab_size,
        embed_dim=128,
        hidden_dim=128,
        num_classes=num_classes,
        dropout=0.3
    )
    lstm_weights = os.path.join(MODELS_DIR, 'lstm_model.pt')
    lstm_model.load_state_dict(torch.load(lstm_weights, map_location=device))
    lstm_model.to(device)
    lstm_model.eval()
    models['LSTM (RNN Group)'] = lstm_model
    
    # Transformer
    transformer_model = TransformerClassifier(
        vocab_size=vocab_size,
        embed_dim=128,
        num_heads=4,
        ff_dim=256,
        num_layers=2,
        num_classes=num_classes,
        max_len=MAX_LEN,
        dropout=0.2
    )
    transformer_weights = os.path.join(MODELS_DIR, 'transformer_model.pt')
    transformer_model.load_state_dict(torch.load(transformer_weights, map_location=device))
    transformer_model.to(device)
    transformer_model.eval()
    models['Transformer Encoder (Transformer Group)'] = transformer_model
    
    return models


# ===== Preprocessing =====
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def encode_text(text, word2id, max_len=MAX_LEN):
    text_clean = clean_text(text)
    ids = [word2id.get(tok, UNK_ID) for tok in text_clean.split()]
    ids = ids[:max_len]
    if len(ids) < max_len:
        ids = ids + [PAD_ID] * (max_len - len(ids))
    return ids


# ===== Prediction =====
def predict(text, model, word2id, id2label):
    ids = encode_text(text, word2id)
    x = torch.tensor([ids], dtype=torch.long, device=device)
    
    with torch.no_grad():
        logits = model(x)
        probs = torch.softmax(logits, dim=1)[0].cpu().numpy()
        pred_id = torch.argmax(logits, dim=1).item()
    
    pred_label = id2label[pred_id]
    confidence = probs[pred_id]
    
    return pred_label, confidence, probs, id2label


# ===== Streamlit UI =====
st.set_page_config(page_title="Text Classification Demo", layout="wide")
st.title("🎯 Text Classification Demo")
st.markdown("**TREC Question Classification** - RNN (LSTM) vs Transformer")

# Load data
word2id, id2label, category_names, vocab_size = load_vocab()
models = load_models(vocab_size, len(category_names))

# Sidebar
st.sidebar.header("⚙️ Configuration")
selected_model = st.sidebar.selectbox(
    "Chọn mô hình:",
    list(models.keys()),
    help="Lựa chọn giữa LSTM hoặc Transformer"
)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Nhập câu hỏi")
    user_input = st.text_area(
        "Nhập text cần phân loại:",
        placeholder="VD: What is the capital of France?",
        height=120,
        label_visibility="collapsed"
    )

with col2:
    st.subheader("📊 Thông tin")
    st.metric("Mô hình", selected_model.split(" (")[0])
    st.metric("Số lớp", len(category_names))
    st.metric("Device", str(device).upper())

# Prediction
if user_input.strip():
    with st.spinner("⏳ Đang dự đoán..."):
        model = models[selected_model]
        pred_label, confidence, probs, id2lab = predict(user_input, model, word2id, id2label)
    
    # Results
    st.success("✅ Dự đoán hoàn tất!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Kết quả")
        st.metric("Lớp dự đoán", pred_label)
        st.metric("Độ tin cậy", f"{confidence:.2%}")
    
    with col2:
        st.subheader("📈 Xác suất tất cả lớp")
        prob_dict = {id2lab[i]: probs[i] for i in range(len(category_names))}
        prob_dict_sorted = dict(sorted(prob_dict.items(), key=lambda x: x[1], reverse=True))
        st.bar_chart(prob_dict_sorted)
    
    # Top predictions
    st.subheader("🏆 Top Predictions")
    top_indices = (-probs).argsort()[:3]
    for rank, idx in enumerate(top_indices, 1):
        with st.expander(f"#{rank}: {id2lab[idx]} ({probs[idx]:.2%})"):
            st.write(f"**Xác suất:** {probs[idx]:.4f}")
    
    # Input summary
    st.subheader("📌 Input Summary")
    st.write(f"**Original:** {user_input}")
    st.write(f"**Cleaned:** {clean_text(user_input)}")
    st.write(f"**Tokens:** {len(clean_text(user_input).split())}")

else:
    st.info("👈 Vui lòng nhập câu hỏi ở trên để bắt đầu dự đoán")

# Footer
st.divider()
st.markdown("""
### 📚 Hướng dẫn sử dụng:
1. **Chọn mô hình** ở sidebar (LSTM hoặc Transformer)
2. **Nhập text** cần phân loại trong textbox
3. **Xem kết quả** - lớp dự đoán + xác suất + biểu đồ
4. **Phân tích** - xem top predictions và tokens

### 🏆 Mô hình availability:
- ✅ LSTM (RNN) - Chất lượng cao, Accuracy=0.8038
- ✅ Transformer - Tốc độ nhanh, Throughput cao

**Ghi chú:** Dữ liệu được chuẩn hóa (lowercase, loại ký tự đặc biệt, ...)
""")
