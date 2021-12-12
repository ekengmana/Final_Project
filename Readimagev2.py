import PIL
import cv2
# from scipy import skimage
import numpy as np
import math
from matplotlib import pyplot as plt
from numpy.core.numeric import count_nonzero

# Hough detection from https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
def readimage(img):
    '''
    A function to read in an image and obtain the radii of droplets
    it detects in an image
    **Parameters** 
        None

    **Returns** 
        radii: *list*
            a list of values indicating the radii of the droplets
        counts: *int*
            the amount of droplets detected
    '''
    # Read image and adjust size
    # img = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('w8_ch1.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.resize(img, (800, 800))
    # blur image
    # img = cv2.medianBlur(img, 3)
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # detect circles in image
    detect_circles = cv2.HoughCircles(img, 
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 70,
                param2 = 20, minRadius = 2, maxRadius = 50)
    radii = []
    for counts in detect_circles[0]:
        radii.append(counts[2])

    counts = len(detect_circles[0])
    # print(detect_circles)
    print(radii)
    if detect_circles is not None:
        detect_circles = np.uint16(np.around(detect_circles))
        for pt in detect_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
    
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (200, 200, 200), 3)
    
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (200, 200, 200), 2)
            # cv2.imshow('image', img)
            # cv2.waitKey(0)
            # detect_circles = np.round(detect_circles[0, :]).astype('int')
            # print(detect_circles)


    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.imwrite('img2_calc.jpg', img)


    return counts, radii

def image_stats(num_circles, radii):
    total_radii = 0
    for radius in radii:
        total_radii += radius
    average = total_radii/num_circles
    plt.hist(radii, 20, (0, 20))
    plt.xlabel('radius (um)')
    plt.ylabel('counts')
    plt.show()

def pix_to_um(img, um, radii):
    # assumes square images
    # image length in pixels converted to length in um
    # the calibration shows ~218 um for a full image length
    dimensions = img.shape
    new_length = um/dimensions[0]
    new_radii = []
    for radius in radii:
        # print(radius)
        rounded = round(new_length * radius, 2)
        new_radii.append(rounded)
    print(new_radii)
    return new_radii

if __name__ == '__main__':
    um = 218
    img = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
    num_circles, radii = readimage(img)
    new_radii = pix_to_um(img, um, radii)
    image_stats(num_circles, new_radii)