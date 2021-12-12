import cv2
import PIL
import imagemod
import numpy as np

def longest_line():
    for i in range(1, 9):
        fptr = 'line_profile/line' + str(i) + '_altered.jpg'
        img = cv2.imread('line_profile/line' + str(i) + '_altered.jpg', cv2.IMREAD_GRAYSCALE)
        value, new_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
        # contours, hierarchy = cv2.findContours(new_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # img_contours = np.zeros(img.shape)
        # cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)
        blur_img = cv2.GaussianBlur(new_img, (9, 9), 0)
        canny_img = cv2.Canny(blur_img, 175, 185)
        # cv2.imshow('contour', canny_img)
        # cv2.waitKey(0)
        detect_circles = cv2.HoughCircles(canny_img, 
                        cv2.HOUGH_GRADIENT, 1.0, 25, param1 = 65,
                    param2 = 14, minRadius = 30, maxRadius = 60)
        if detect_circles is not None:
            detect_circles = np.uint16(np.around(detect_circles))
            for pt in detect_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
        
                # Draw the circumference of the circle.
                cv2.circle(canny_img, (a, b), r, (255, 255, 255), 2)
        
                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(canny_img, (a, b), 1, (0, 0, 0), 2)
                # cv2.imshow('image', img)
                # cv2.waitKey(0)
                # detect_circles = np.round(detect_circles[0, :]).astype('int')
                # print(detect_circles)
            cv2.imshow('image', canny_img)
            cv2.waitKey(0)
            # cv2.imwrite('altered_calc.jpg', new_img)

        # cv2.imshow('canny', canny_img)
        # cv2.waitKey(0)
    pass


if __name__ == '__main__':
    for i in range(1, 9):
        fptr = str('line' + str(i))
        imagemod.alter_image('line_profile/' + fptr, 30)
    longest_line()
