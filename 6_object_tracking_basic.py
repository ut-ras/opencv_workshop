# Import the necessary python libraries
import numpy as np
import cv2

# Create a range in the HSV color space that we want to isolate (mask)
redUpper = (15, 255, 255)
redLower = (0, 86, 6)
blueUpper = (133, 255, 255)
blueLower = (87, 86, 6)

# Set up a video feed from your system's default web cam
cap = cv2.VideoCapture(0)
 
# This loop runs continuously, bringing in new frames and processing them each time through the loop
while(True):

    # Read a frame from the webcam
    ret, frame = cap.read()

    # Resize the frame
    frame = cv2.resize(frame, (640, 360))

    # Convert to HSV (hue, saturation, value) color space
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary image where pixels that fall in range are white and the rest are black
    mask = cv2.inRange(frameHSV, redLower, redUpper)

    # These transformations help clean up a noisy image
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find and draw contours
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    # Uncomment the line below to see the boundaries found by findContours
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    # Only proceed if there are contours
    if len(contours) > 0:
        # Find the contour that has the largest area
        c = max(contours, key=cv2.contourArea)
        # Circumscribe that contour
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        # If the circle is large enough
        if radius > 20:
            # Draw the circle on frame
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

    # Display the frame in a window
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # This code will quit the program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# This code releases your system's webcam and closes all open windows
cap.release()
cv2.destroyAllWindows()
