# ĐẠI HỌC BÁCH KHOA
## Khoa Khoa học và Kỹ thuật Máy tính

# CO5085 - Học sâu và ứng dụng trong thị giác máy tính

## Thông tin nhóm
- **Tên nhóm:** GROUP 02
- **Giảng viên môn học:** TS. Lê Thành Sách

## Thành viên
1. Lý Minh Trung - 2570349
2. Ngô Nhất Toàn - 2570515
3. Nguyễn Thái Thành Đạt - 2570387

## Link đến từng bài tập
- [Exercise](https://github.com/trungly-hcmut/CO5085_DeepLearning_CV/tree/main/exercise)
- [Assignment 1](https://github.com/trungly-hcmut/CO5085_DeepLearning_CV/tree/main/assignment_1)
- [Assignment 2](https://github.com/trungly-hcmut/CO5085_DeepLearning_CV/tree/main/assignment_2)

## 1) Bài tập cơ bản: Phân loại ảnh với các mô hình học sâu cơ bản
**Mục tiêu:** Nắm vững cách xây dựng vòng lặp huấn luyện thủ công và các kiến trúc mạng từ đơn giản đến phức tạp.

**Tập dữ liệu:** Chọn một trong các tập dữ liệu nhỏ như **MNIST**, **Fashion-MNIST**, hoặc **CIFAR-10**.

**Nội dung thực hiện:**
- Xây dựng 4 mô hình cơ bản: **Softmax Regression**, **MLP**, **CNN**, và **Vision Transformer** (sử dụng API PyTorch).
- **Vòng lặp huấn luyện (Training Loop):** Tự viết bằng PyTorch (không dùng API cấp cao như Lightning).
- **Tự hiện thực Transformer:** Xây dựng `TransformerEncoder` từ các phép toán cơ bản (`Linear`, `LayerNorm`, `einsum`) và so sánh với bản của PyTorch.
- **Kiến trúc kết hợp:** Thử nghiệm kết hợp **CNN-Transformer** hoặc các phương pháp tokenize/embed ảnh khác nhau.
- **Mô hình RNN:** Sử dụng **LSTM/GRU** để phân loại ảnh bằng cách biến ảnh thành chuỗi (theo hàng, cột hoặc patch).

**Hạn nộp:** **01/04/2026**.

## 2) Bài tập lớn số 1: Phân loại dữ liệu đa phương thức
**Mục tiêu:** Vận dụng các mô hình pretrained để giải quyết bài toán phân loại trên 3 loại dữ liệu khác nhau.

**Yêu cầu tập dữ liệu:**
- 3 loại: **Ảnh (Image)**, **Văn bản (Text)**, và **Đa phương thức (Multimodal: Ảnh + Văn bản)**.
- Ràng buộc: Ít nhất **5 lớp**, kích thước tập train $\ge 5.000$ mẫu (cho ảnh/văn bản).

**Yêu cầu kỹ thuật:**
- Dữ liệu ảnh: So sánh **CNN** vs **Vision Transformer (ViT)**.
- Dữ liệu văn bản: So sánh **RNN (LSTM)** vs **Transformer**.
- Dữ liệu đa phương thức: So sánh **Zero-shot** vs **Few-shot classification**.

**Sản phẩm:** Báo cáo, mã nguồn, video demo và landing page trên GitHub Pages.

**Hạn nộp:** **23h59, ngày 25/03/2026**.

## 3) Bài tập lớn số 2: Các bài toán nâng cao trong thị giác máy tính
**Mục tiêu:** Triển khai chuyên sâu một chủ đề cụ thể trong thị giác máy tính.

**Chủ đề lựa chọn (chọn 1 trong 4):**
- **Phân đoạn ảnh (Segmentation):** Semantic, Instance hoặc Panoptic segmentation.
- **Phát hiện đối tượng (Object Detection):** YOLO, Faster R-CNN, DETR.
- **Định danh đối tượng (Recognition/ReID):** Nhận diện khuôn mặt, Re-identification.
- **Tạo sinh hình ảnh (Image Generation):** GAN, VAE, Diffusion models.

**Yêu cầu kỹ thuật:**
- So sánh ít nhất hai phương pháp hoặc hai biến thể kiến trúc/backbone khác nhau.
- Sử dụng các metric chuẩn tương ứng:
	- **IoU** (Phân đoạn)
	- **mAP** (Phát hiện)
	- **Accuracy/Rank@k** (Định danh)
	- **FID/IS** (Tạo sinh)

**Sản phẩm:** Cập nhật landing page từ BTL1, nộp báo cáo slide (PDF), mã nguồn và video.

**Hạn nộp:** **Dự kiến 08/04/2026**.
