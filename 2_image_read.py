import numpy as np
import cv2

# Reads in the image 'krabs.jpg' from the current directory
img = cv2.imread('krabs.jpg')

# Display the image in a window
cv2.imshow('image',img)

# Wait for a key to be pressed and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()