# Final_Project
This is a project containing a few codes to analyze different aspects of an image.
The images are from my research on DNA droplets, and the code is split into 3 main parts, all of which can use the imagemod.py file to alter the contrast of 
the images of interest.

Readimage allows one to look at an image and detect the circles aka droplets in the image. It uses Hough transform in OpenCV by doing a Canny Edge Detection, then using the
Canny processed image to try and detect circular structures. In addition, the code has a function to automatically blur/increase the contrast in a while loop while also changing the 
threshold  of detection of droplets, so that way smaller droplets or less-in depth droplets (since it is a 2D image of a 2D spacce) are detected first,
then they are colored in before attemting to find more droplets that are brighter/more in view/bigger. This is the attempt to counter the large amount of noise present in images
After detecting droplets in the image, statistics are calculated and plotted in a histogram after adjusting the pixels to micrometer values.
2 images are shown as an example for this code working, one containing more noise compared to the other. 

Recolor is a simple code that takes images that were acquired using different fluorescence channels, color codes them, then merges them together into an overlayed image.
this allows one to see the colocalization of droplets (or lack there of).

lineprofile attempts to draw scan-lines over a series of images taken over time to measure the droplets fusing together. The attempt for this is to adjust the contrast in a very 
noisy image before trying to find the droplets. Then, the program attempts to find the longest line from one far end of 1 droplet to the opposite far end of the other droplet.
The scan-lines are then plotted to measure the distance and to confirm wen fusion is fully complete. 
