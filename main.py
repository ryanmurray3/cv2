# Ryan Murray
# Convert Image to grayscale

import cv2

image = cv2.imread('/Users/ryanmurray/Desktop/Vision_Board_Images 24 27.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)         #cvtColor function with built in color to gray

cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)          # prevents windows from closing based on time rather the user will press any key on the keyboard
cv2.destroyAllWindows()