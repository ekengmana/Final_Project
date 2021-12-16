
from PIL import Image
import cv2
# from scipy import skimage
import numpy as np
import imagemod
from matplotlib import pyplot as plt
from numpy.core.numeric import count_nonzero

# Hough detection from https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
def readimage(filename, threshold_limit = 50, iteration_limit = 2):
    '''
    A function to read in an image and obtain the radii of droplets
    it detects in an image
    **Parameters** 
        img: *cv2 image*
            A cv2 image to be manipulated and altered to calculate the droplets present

    **Returns** 
        radii: *list*
            a list of values indicating the radii of the droplets
        total_counts: *int*
            the amount of droplets detected overall after all iterations
    '''
    base_name = '.'.join(filename.split('.')[0:-1])
    total_counts = 0
    blur = (5, 5)
    # blur level
    num_counts = -1
    radii = []
    iteration = 0
    # the iteration of altering and detecting droplets
    threshold = 0
    # the threshold value for when creating more contrast in the image
    # using imagemod.py
    droplets = []
    # store detected droplets to draw for clear image of detected droplets
    while num_counts != 0:
        num_counts = 0
        # reset the number of counts from the previous iteration
        iteration = iteration + 1
        # alter the iteration
        # if iteration == 1:
        imagemod.alter_image(base_name, iteration, threshold)
        if iteration != 1:
            imagemod.draw_filled(base_name + '_altered' + str(iteration) + '.jpg', iteration, 'img_calc' + str(iteration - 1) + '.jpg')
            # fill in the previous iteration's detected droplets
            contrast_img = cv2.imread(base_name + '_filled' + str(iteration - 1) + '.jpg', cv2.IMREAD_GRAYSCALE)
        else:
            contrast_img = cv2.imread('img_altered' + str(iteration) + '.jpg', cv2.IMREAD_GRAYSCALE)
        # create and open a more contrasted image
        # cv2.imshow('image', contrast_img)
        # cv2.waitKey(0)
        blur_img = cv2.GaussianBlur(contrast_img, blur, 0)
        # cv2.imshow('image', blur_img)
        # cv2.waitKey(0)
        detect_circles = cv2.HoughCircles(blur_img, 
                        cv2.HOUGH_GRADIENT, 1, 20, param1 = 320,
                    param2 = 10, minRadius = 2, maxRadius = 40)
            # The parameters set here can be adjusted if there are issues in circle detection,
            # but these are the ones I've found that give the most accurate detections
            # based on the contrast applied
        # print(type(detect_circles[0]))
        if detect_circles is not None:
            for counts in detect_circles[0]:
                radii.append(counts[2])

            num_counts = len(detect_circles[0])
        else:
            num_counts = 0
        # print(detect_circles)
        # print(radii)
        if detect_circles is not None:
            detect_circles = np.uint16(np.around(detect_circles))
            for pt in detect_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
                droplets.append([a, b, r])
        
                # Draw the circumference of the circle.
                # cv2.circle(blur_img, (a, b), r, (100, 100, 100), 3)
        
                cv2.circle(blur_img, (a, b), 1, (0, 0, 0), 2 * r + 8)
                # draw over the detected circle so it will not be detected again after
                # imagemod.drawfilled
            cv2.imwrite(base_name + '_calc' + str(iteration) + '.jpg', blur_img)

        # blur = (blur[0] + 2, blur[1] + 2)

        total_counts += num_counts
        threshold += 25
        if threshold > threshold_limit:
            # threshold limit can be adjusted as user would like
            break
        elif iteration >= iteration_limit:
            break
            # number of iterations performed can be adjusted as user would like
        # print(threshold)
    img_droplets = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    for droplet in droplets:
        cv2.circle(img_droplets, (droplet[0], droplet[1]), droplet[2], (200, 200, 200), 2)
    cv2.imwrite(base_name + '_droplets.jpg', img_droplets)
         
    # print(total_counts, len(radii))
    return total_counts, radii

def image_stats(num_circles, radii):
    '''
    A function to calculate statistics of the droplets detected and their range in radius values
    **Parameters**
        num_circles: *int*
            The number of circles detected in a given image
        radii: *list, int*
            A list of radius values from the detected circles/droplets

    '''
    total_radii = 0
    for radius in radii:
        total_radii += radius
    average = total_radii/num_circles
    # bin_width = np.linspace(0, 15, 30, endpoint = False)
    # print(bins)
    plt.hist(radii, 10, color = 'b', edgecolor = 'k')
    # plt.xticks(ticks = 1)
    plt.axvline(average, color = 'r', linestyle = 'dashed', linewidth = 1.5)
    # displays a vertical line indicating the average
    plt.xlabel('radius (um)')
    plt.ylabel('counts')
    plt.show()

def pix_to_um(img, um, radii):
    '''
    converts image pixels into real-world distances, in this case micrometers
    **Parameters**
        img: *image*
            image opened with cv2 to be used to obtain dimensions
        um: *int*
            the conversion value in micrometers, obtained outside of this program
        radii: *list, float*
            a list of radii obtained from readimage()
            values are in pixels
    '''
    dimensions = img.shape
    # acquire the dimensions of the image
    new_length = um/dimensions[0]
    # convert pixels to micrometers
    new_radii = []
    # list for the new values in micrometers
    for radius in radii:
        # print(radius)
        rounded = round(new_length * radius, 2)
        # clean up values
        new_radii.append(rounded)
    # print(new_radii)
    return new_radii

if __name__ == '__main__':
    um = 218
    cv2_img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
    num_circles, radii = readimage('img.jpg', 50, 2)
    new_radii = pix_to_um(cv2_img, um, radii)
    image_stats(num_circles, new_radii)