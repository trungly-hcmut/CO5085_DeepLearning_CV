# Exercise - Deep Learning Fundamentals on CIFAR-10

## Thông tin
- **Khóa học:** CO5085 - Deep Learning & Computer Vision
- **Giảng viên:** TS. Lê Thành Sách

## Thành viên
1. Lý Minh Trung - 2570349
2. Ngô Nhất Toàn - 2570515
3. Nguyễn Thái Thành Đạt - 2570387

---

## Mục tiêu
Folder này bao gồm **5 phần bài tập thực hành** nhằm xây dựng kỹ năng cơ bản trong Deep Learning:
- Tiền xử lý dữ liệu (Data Preprocessing)
- Xây dựng mô hình CNN từ đầu (CNN from Scratch)
- So sánh kiến trúc (Architecture Comparison)
- Kỹ thuật regularization & optimization
- Phân loại hình ảnh với RNN/LSTM/GRU

Toàn bộ bài tập sử dụng dataset **CIFAR-10** để thực hành trên dữ liệu chuẩn hoá.

---

## Cấu trúc bài tập

### **Phần 1-2: CNN Cơ bản & Tiền xử lý dữ liệu**
[Notebook: Exercise_part_1_2.ipynb](./Exercise_part_1_2.ipynb)

**Nội dung:**
- Load và khám phá dataset CIFAR-10
- Tiền xử lý dữ liệu (normalization, augmentation)
- Xây dựng mô hình CNN đơn giản từ đầu
- Huấn luyện và đánh giá kết quả

**Kỹ năng:** Data loading, exploratory analysis, CNN architecture design

---

### **Phần 3-4: So sánh kiến trúc CNN & Kỹ thuật Regularization**
[Notebook: Exercise_part_3_4.ipynb](./Exercise_part_3_4.ipynb)

**Nội dung:**
- So sánh các kiến trúc CNN khác nhau (simple vs deep models)
- Áp dụng kỹ thuật regularization:
  - Dropout
  - Batch Normalization
  - L2 Regularization
- Tối ưu hóa hyperparameters

**Kỹ năng:** Architecture design, regularization techniques, hyperparameter tuning

---

### **Phần 5: Phân loại ảnh với RNN/LSTM/GRU**
[Notebook: Exercise_part_5.ipynb](./Exercise_part_5.ipynb)

**Nội dung:**
- Chuyển ảnh 2D thành chuỗi (sequence) để sử dụng RNN
- So sánh hai kiến trúc RNN:
  - **LSTM** (Long Short-Term Memory)
  - **GRU** (Gated Recurrent Unit)
- So sánh cách encoding: row sequence vs patch sequence
- Đánh giá và so sánh hiệu năng

**Kỹ năng:** RNN architecture, sequence modeling, attention mechanisms

---

## Dữ liệu (Data)

Dataset **CIFAR-10** được lưu tại thư mục `data/`:
- Train set: 50,000 ảnh
- Test set: 10,000 ảnh
- 10 lớp: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
- Kích thước: 32×32 RGB

**Download tự động:** Các notebook sẽ tự động download dataset nếu chưa có.

---

## Requirements

**Python 3.8+**

**Thư viện chính:**
- PyTorch
- Torchvision
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- tqdm

---

## Hướng dẫn sử dụng

### Chạy từng phần:

1. **Mở Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Hoặc dùng VS Code:**
   - Mở file `.ipynb` trong VS Code
   - Chạy từng cell bằng phím `Shift+Enter`

3. **Toàn bộ notebooks có thể chạy độc lập** (mỗi phần tải dữ liệu riêng)

---

## Cấu trúc thư mục

```
exercise/
├── Exercise_part_1_2.ipynb    # Phần 1-2
├── Exercise_part_3_4.ipynb    # Phần 3-4
├── Exercise_part_5.ipynb      # Phần 5
├── README.md                  # File này
└── latex/
    └── main.tex               # Báo cáo LaTeX
```

---

## Notes

- Tất cả notebooks được thiết kế để **chạy độc lập** trên bất kỳ máy nào có Python và CUDA (nếu có GPU)
- Đặt seed cố định để kết quả **reproducible** giữa các lần chạy
- Sử dụng **Gradient Clipping** và **Learning Rate Scheduling** để ổn định huấn luyện RNN
- Hỗ trợ cả CPU và GPU (tự động detect)

---

## Lưu ý

- Lần chạy đầu tiên sẽ mất vài phút để download CIFAR-10 (~200MB) nếu chưa có
- Huấn luyện RNN trên CPU sẽ khá chậm, khuyến khích dùng GPU
- Có thể điều chỉnh `batch_size`, `epochs`, `hidden_size` trong Config tùy theo máy của bạn

---

## Tham khảo

- CIFAR-10 Dataset: https://www.cs.toronto.edu/~kriz/cifar.html
- PyTorch Documentation: https://pytorch.org/docs/

---