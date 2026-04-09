import cv2
import os

os.makedirs("output", exist_ok=True)

# load test image
img = cv2.imread("test.jpg")

# load haar cascade (built into opencv)
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30,30)
)

for (x,y,w,h) in faces:
    cv2.rectangle(
        img,
        (x,y),
        (x+w,y+h),
        (0,255,0),
        2
    )

cv2.imwrite("output/detections.jpg", img)

print("Faces detected:", len(faces))
print("Output saved to output/detections.jpg")