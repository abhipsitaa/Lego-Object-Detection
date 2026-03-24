from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")

brick_info = {
    "2x2": {"part_id": "3003", "name": "Brick 2x2"},
    "2x4": {"part_id": "3001", "name": "Brick 2x4"},
    "1x4": {"part_id": "3010", "name": "Brick 1x4"},
    "2x3": {"part_id": "3002", "name": "Brick 2x3"},
}

results = model(
    "LEGO-OBJECT-DETECTION-2/test/images/",
    conf=0.1,
    save=True
)

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label in brick_info:
            print("\nDetected:", brick_info[label]["name"])
            print("Part ID:", brick_info[label]["part_id"])

