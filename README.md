# 🧱 LEGO Object Detection using YOLOv8

A deep learning-based object detection system that detects and localizes LEGO bricks in images using YOLOv8 (You Only Look Once).

---

## 📌 Project Overview

This project was developed as part of an internship to build a real-time LEGO brick detection system. It uses the YOLOv8 nano model trained on a custom LEGO dataset to accurately identify and draw bounding boxes around LEGO pieces in images.

---

## 🚀 Features

- Detects LEGO bricks in images with high accuracy
- Trained on a custom annotated LEGO dataset (640x640 resolution)
- Achieves ~99% precision and ~74% recall on the validation set
- Fast inference (~7ms per image)
- Bounding box visualization with confidence scores

---

## 🛠️ Tech Stack

- **Python 3.x**
- **YOLOv8** (Ultralytics)
- **PyTorch**
- **OpenCV**
- **Kaggle** (for GPU training)

---

## 📁 Project Structure

```
Lego-Object-Detection/
│
├── train_yolo.py         # Script to train YOLOv8 on the LEGO dataset
├── train.py              # Alternative training script
├── detect.py             # Run detection on images
├── detection.py          # Detection utilities
├── download_dataset.py   # Script to download the dataset
├── data.yaml             # Dataset configuration file
├── .gitignore
└── README.md
```

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/abhipsitaa/Lego-Object-Detection.git
cd Lego-Object-Detection
```

2. **Install dependencies**
```bash
pip install ultralytics opencv-python
```

---

## 🗂️ Dataset

- **Source:** [LEGO Object Detection Dataset on Kaggle](https://www.kaggle.com/datasets/abhipsitasarkar/lego-object-detection)
- **Classes:** 1 (lego)
- **Training images:** ~2800
- **Validation images:** 703
- **Image size:** 640x640

To download the dataset, run:
```bash
python download_dataset.py
```

---

## 🏋️ Training

To train the model from scratch:
```bash
python train_yolo.py
```

Training configuration:
- **Model:** YOLOv8n (nano)
- **Epochs:** 50
- **Image size:** 640
- **Batch size:** 16

---

## 🔍 Detection

To run detection on your images:
```bash
python detect.py
```

---

## 📊 Results

| Metric | Value |
|--------|-------|
| Precision | 99.3% |
| Recall | 74.4% |
| mAP@50 | 74.3% |
| mAP@50-95 | 59.8% |
| Inference Speed | ~7ms/image |

---

## 🖼️ Sample Output

The model successfully detects and draws bounding boxes around individual LEGO bricks in images, even in dense scenes with hundreds of overlapping pieces.

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [LEGO Object Detection Dataset](https://www.kaggle.com/datasets/abhipsitasarkar/lego-object-detection)
- Kaggle for providing free GPU resources
