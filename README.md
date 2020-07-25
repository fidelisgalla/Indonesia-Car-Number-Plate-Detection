# Indonesia Car Number Plate Detection

## Overview
This repository will show the method for detecting Indonesian plate car using Python OpenCV (non deep learning method)(`plate_detection_indonesia.py` file) . The method will use __contour detection concept__. 

## Steps
1. The first step is loading the image. We will use this image

![Fig1](https://github.com/fidelisgalla/Indonesia-Car-Number-Plate-Detection/blob/master/plate1.jpg?raw=true)

2. The next step is image processing. It plays very important role for contour detection. In this code, for image processing, we will conduct : conversion from colored image to grayscale, then filtering, after that we conduct the adaptive Threshold. Adaptive threshold is applied because of its ability to handle different illuminaton intensity problem in an image. 

3. After that, we can find the contours using `cv.findContours()` method and we apply ROI (region of interest) technique to find the plate area. 

4. __Image to string__ with Pytesseract and the result is :

![Fig2](https://github.com/fidelisgalla/Indonesia-Car-Number-Plate-Detection/blob/master/result.jpg?raw=true)

The code still needs improvement, especially for the image to text process.
