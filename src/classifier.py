import numpy as np
from ultralytics import YOLO

class DroneClassifier:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def classify(self, frame, bbox):
        x, y, w, h = bbox
        crop = frame[y:y+h, x:x+w]
        if crop.size == 0:
            return "unknown", 0.0
        res = self.model.predict(crop, verbose=False)[0]
        if len(res.boxes) == 0:
            return "unknown", 0.0
        top = max(res.boxes, key=lambda b: float(b.conf[0]))
        return self.model.names[int(top.cls[0])], float(top.conf[0])
