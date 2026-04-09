import cv2
import numpy as np
import os
from datetime import datetime

os.makedirs("output", exist_ok=True)

img = np.zeros((400,600,3), dtype=np.uint8)

cv2.putText(
    img,
    "APD Jenkins CI/CD Pipeline",
    (30,200),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0,255,0),
    2
)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cv2.putText(
    img,
    timestamp,
    (30,250),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (255,255,255),
    1
)

cv2.imwrite("output/detections.jpg", img)

print("Output saved to output/detections.jpg")
