import PIL
import cv2
# from scipy import skimage
import numpy as np
import math
from matplotlib import pyplot as plt

# Hough detection from https://www.geeksforgeeks.org/circle-detection-using-opencv-python/

# Read image and adjust size
img = cv2.imread('1h15mRNAse.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('w8_ch1.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, (800, 800))
# blur image
img = cv2.medianBlur(img, 7)

# detect circles in image
detect_circles = cv2.HoughCircles(img, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 30,
               param2 = 40, minRadius = 1, maxRadius = 40)

print(len(detect_circles[0]))
if detect_circles is not None:
    detect_circles = np.uint16(np.around(detect_circles))
    for pt in detect_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 1)
  
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 2)
        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        # detect_circles = np.round(detect_circles[0, :]).astype('int')
        # print(detect_circles)


cv2.imshow('image', img)
cv2.waitKey(0)
