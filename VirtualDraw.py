import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.flip(img,1)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

