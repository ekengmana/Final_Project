# Final_Project
This is a project containing a few codes to analyze different aspects of an image.
The images are from my research on DNA droplets, and the code is split into 3 main parts, all of which can use the imagemod.py file to alter the contrast of 
the images of interest.

Readimage allows one to look at an image and detect the circles aka droplets in the image. It uses Hough transform in OpenCV by doing a Canny Edge Detection, then using the
Canny processed image to try and detect circular structures. In addition, the code has a function to automatically blur/increase the contrast in a while loop while also changing the threshold of detection of droplets, so that way smaller droplets or less-in depth droplets (since it is a 2D image of a 2D spacce) are detected first,
then they are colored in before attempting to find more droplets that are brighter/more in view/bigger. This is the attempt to counter the large amount of noise present in images
The altered images are saved separately for the file to work as well as for the user to know what is happening, in addition to an annotated image of the original file showing what droplets were detected.
After detecting droplets in the image, statistics are calculated and plotted in a histogram after adjusting the pixels to micrometer values.
img.jpg is used as an example for this code working, one containing more noise compared to the other. 
Latest version: thresholds have been optimized for the given image and drawing in previously detected droplets is successful. Not all droplets are detected, but more are detected as well as more accurately compared to version one.

Recolor is a simple code that takes images that were acquired using different fluorescence channels, color codes them, then merges them together into an overlayed image.
this allows one to see the colocalization of droplets (or lack there of).

lineprofile is unfinished but was attempted. It attempts to draw a line over a series of images taken over time to measure the droplets fusing together. The attempt for this is to adjust the contrast in a very 
noisy image before trying to find the droplets. Then, the program attempts to find the longest line from one far end of 1 droplet to the opposite far end of the other droplet.
The scan-lines are then plotted to measure the distance and to confirm wen fusion is fully complete. 

Modules required:
numpy
matplotlib
cv2
PIL

Credits to the following videos/sources:
Hough detection from https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
"Finding the Edges - Sobel Operator" Computerphile, https://www.youtube.com/watch?v=uihBwtPIBxM
"Canny Edge Detector" Comuterphile, https://www.youtube.com/watch?v=sRFM5IEqR2w
"How Circle Hough Transform Works" Thales Sehn Korting, https://www.youtube.com/watch?v=Ltqt24SQQoI
