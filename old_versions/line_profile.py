import cv2
import PIL
import imagemod
import numpy as np

def longest_line():
    for i in range(1, 9):
        fptr = 'line_profile/line' + str(i) + '_altered.jpg'
        img = cv2.imread('line_profile/line' + str(i) + '_altered.jpg', cv2.IMREAD_GRAYSCALE)
        blur_img = cv2.GaussianBlur(img, (7, 7), 0)
        # canny_img = cv2.Canny(blur_img, 50, 100)
        detect_circles = cv2.HoughCircles(blur_img, 
                        cv2.HOUGH_GRADIENT, 0.8, 20, param1 = 80,
                    param2 = 10, minRadius = 50, maxRadius = 60)
        # if detect_circles is not None:
        #     detect_circles = np.uint16(np.around(detect_circles))
        #     for pt in detect_circles[0, :]:
        #         a, b, r = pt[0], pt[1], pt[2]
        
        #         # Draw the circumference of the circle.
        #         cv2.circle(blur_img, (a, b), r, (255, 255, 255), 2)
        
        #         # Draw a small circle (of radius 1) to show the center.
        #         cv2.circle(blur_img, (a, b), 1, (0, 0, 0), 2)
        #         # cv2.imshow('image', img)
        #         # cv2.waitKey(0)
        #         # detect_circles = np.round(detect_circles[0, :]).astype('int')
        #         # print(detect_circles)
        #     cv2.imshow('image', blur_img)
        #     cv2.waitKey(0)
        #     # cv2.imwrite('altered_calc.jpg', new_img)

        # cv2.imshow('canny', canny_img)
        # cv2.waitKey(0)
    pass


if __name__ == '__main__':
    for i in range(1, 9):
        fptr = str('line' + str(i))
        imagemod.alter_image('line_profile/' + fptr, 30)
    longest_line()
