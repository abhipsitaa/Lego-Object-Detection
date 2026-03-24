from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")  # lightweight

# Train model
model.train(
    data="LEGO-OBJECT-DETECTION-2/data.yaml",
    epochs=50,
    imgsz=640
)