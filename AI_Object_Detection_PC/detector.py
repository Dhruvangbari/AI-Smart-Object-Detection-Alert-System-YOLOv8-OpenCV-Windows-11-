from ultralytics import YOLO
from config import TARGET_CLASSES, CONFIDENCE_THRESHOLD

model = YOLO("yolov8n.pt")

def detect(frame):
    results = model(frame, verbose=False)[0]
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        confidence = float(box.conf[0])

        if label in TARGET_CLASSES and confidence > CONFIDENCE_THRESHOLD:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append((label, confidence, x1, y1, x2, y2))

    return detections
