import cv2
import numpy as np

class SkyDetector:
    """Детекция мелких объектов на фоне неба (background subtraction + blob)."""
    def __init__(self, min_area=20, max_area=5000):
        self.bg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25)
        self.min_area = min_area
        self.max_area = max_area

    def detect(self, frame):
        fg = self.bg.apply(frame)
        _, th = cv2.threshold(fg, 200, 255, cv2.THRESH_BINARY)
        th = cv2.morphologyEx(th, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        boxes = []
        for c in contours:
            a = cv2.contourArea(c)
            if self.min_area < a < self.max_area:
                boxes.append(cv2.boundingRect(c))
        return boxes
