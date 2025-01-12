import cv2
import numpy as np

# Read the image
image = cv2.imread('assignment-001-given.jpg')

# Create a transparent overlay to simulate reduced opacity
overlay = image.copy()

# Draw a black rectangle with reduced opacity
cv2.rectangle(overlay, (800, 200), (1300, 100), (0, 0, 0), -1)

# Blend the overlay with the original image (0.3 opacity for the black background)
cv2.addWeighted(overlay, 0.3, image, 1 - 0.3, 0, image)

# Add the green text over the blended image
cv2.putText(image, 
            'RAH972U',
            (830,180),
            cv2.FONT_HERSHEY_SIMPLEX,
            3,
            (0,255,0),
            5,
            cv2.LINE_4)

# Draw a rectangle on the image
cv2.rectangle(image, (250,200), (980,920), (0,255,0), 7)

# Name the window and display the image
cv2.namedWindow('Image window', cv2.WINDOW_NORMAL)
cv2.imshow('Image window', image)

# Wait for the user to press a key
cv2.waitKey(0)

# Save the image
cv2.imwrite('result.jpg', image)

# Destroy the window
cv2.destroyAllWindows()
