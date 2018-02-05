# Import the necessary python libraries
import numpy as np
import cv2

# This code sets up a video feed from your system's default web cam
cap = cv2.VideoCapture(0)
 
# This loop runs continuously, bringing in new frames and processing each time through the loop
while(True):
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Display the frame in a window
    cv2.imshow('frame', frame)

    # This code will quit the program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release system webcam and close all windows
cap.release()
cv2.destroyAllWindows()