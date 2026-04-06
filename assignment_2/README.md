# Assignment 2 - Object Detection Models Comparison

## Thông tin nhóm
- **Tên nhóm:** GROUP 02
- **Giảng viên môn học:** TS. Lê Thành Sách

## Thành viên
1. Lý Minh Trung - 2570349
2. Ngô Nhất Toàn - 2570515
3. Nguyễn Thái Thành Đạt - 2570387

Repository này bao gồm các thí nghiệm so sánh các mô hình Object Detection: YOLOv11, DETR, và Fast R-CNN trên tập dữ liệu COCO.

---

## 1 YOLOv11 (You Only Look Once v11)
Huấn luyện và đánh giá mô hình YOLOv11 trên tập dữ liệu COCO subset.

**Notebooks:**
- [YOLOv11 COCO Subset Training](./yolov11_coco_subset.ipynb) - Huấn luyện trên subset
- [YOLOv11 COCO Training](./yolov11_coco.ipynb) - Huấn luyện trên COCO đầy đủ
- [YOLOv11 COCO Subset (Colab)](./yolov11_coco_subset_colab.ipynb) - Phiên bản Colab tối ưu

**Trọng số:** 
- [yolo11n.pt](https://drive.google.com/file/d/1BJHzMmCsMiNrqj0qTze208AVPR4rXTT7/view?usp=drive_link) - Nano model
- [yolo11s.pt](https://drive.google.com/file/d/1g9haRHglpqFhk2uYaMwiHD09sINQSzPw/view?usp=drive_link) - Small model

---

## 2 DETR (Detection Transformer)
Huấn luyện và đánh giá mô hình DETR (ResNet-50 backbone) trên tập dữ liệu COCO.

**Notebook:**
- [DETR Training](./DETR_Training.ipynb)

**Trọng số:**
- [detr_r50_w.pt](https://drive.google.com/file/d/1o6znuvOUpqfkmDGpScQNHB5BDJAT1_9W/view?usp=drive_link) - DETR với ResNet-50 backbone

**Kết quả:**
- Training history: `detr_runs/training_history.csv`
- Metrics: `detr_runs/metrics.json`

---

## 3 Faster R-CNN
Huấn luyện và đánh giá Faster R-CNN trên tập dữ liệu COCO.

**Notebook:**
- [Fast R-CNN Training](./Fast_RCNN_Training.ipynb)

**Trọng số:**
- [fast_rcnn_w.pth](https://drive.google.com/file/d/10uIO2dyma45NMiX0LAHzp8-FFyJN3AMY/view?usp=drive_link) - Faster R-CNN model

---

## 4 Model Comparison
So sánh chi tiết hiệu suất của ba mô hình (YOLOv11, DETR, Faster R-CNN).

**Notebook:**
- [Model Comparison](./model_comparison_yolo_fast_rcnn.ipynb)

**Kết quả so sánh:**
- CSV format: `reports/comparison_metrics.csv`
- JSON format: `reports/comparison_metrics.json`

---

## 5 Live Inference Demo
Demo thực thi real-time detection trên hình ảnh/video.

**Notebook:**
- [Demo Live Inference](./demo_live_inference.ipynb)

---

## 6 Dữ liệu (Dataset)
- **COCO Subset:** Tập con của COCO 2017 được sử dụng để huấn luyện nhanh hơn
  - Annotations: `coco/annotations/`
  - Validation images: `coco/val2017/`
- **COCO Config:** `coco_subset.yaml` - Cấu hình tập dữ liệu

---

## 7 Kết quả & Báo cáo
Các báo cáo tổng hợp và so sánh kết quả được lưu trong:
- `reports/` - Báo cáo và kết quả so sánh
- `detr_runs/` - Training logs và checkpoints của DETR
- `runs/` - YOLOv11 training artifacts

---

## 8 Tài liệu tham khảo
- [YOLOv11 Official Repository](https://github.com/ultralytics/ultralytics)
- [DETR Official Repository](https://github.com/facebookresearch/detr)
- [Faster R-CNN Paper](https://arxiv.org/abs/1506.01497)
- [COCO Dataset](https://cocodataset.org/)

---

## Notes
- Các notebooks được thiết kế để chạy độc lập trên Google Colab hoặc locally
- Để chạy locally, cần cài đặt: `torch`, `torchvision`, `ultralytics`, `requests`, `opencv-python`, v.v.
- Các mô hình pretrained sẽ được tải xuống tự động nếu cần
- Kết quả và so sánh được trình bày trực tiếp trong từng file notebook
