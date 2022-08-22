import cv2
import numpy as np

cap = cv2.VideoCapture('video1.mp4')

while(True):
    ret, frame = cap.read()
    edge = 255- cv2.Canny(frame, 50, 120)
    cv2.imshow('edge',edge)
    cv2.waitKey(1)
