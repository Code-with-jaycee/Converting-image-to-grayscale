# jaycee
# Date: 27 july 2021
# Essential functions
# Stop: 38

import cv2 as cv

img = cv.imread("images/jaycee.jpg")
#cv.imshow('Cat', img)


def rescalling(frame, scale=0.375):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


newImg = rescalling(img)
cv.imshow('new image', newImg)
# Converting to gray scale.
gray = cv.cvtColor(newImg, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Converting to Blur
blur = cv.GaussianBlur(newImg, (9, 9), cv.BORDER_DEFAULT)
# (3,3) always odd numbers
cv.imshow("Blur", blur)

# Finding edges (Cascade)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny edge", canny)

# Dilating the image
dilated = cv.dilate(canny, (9, 9), iterations=3)
cv.imshow("Dilated", dilated)

while cv.waitKey() == ('q'):
    break

