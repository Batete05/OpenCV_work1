README for Image Text and Rectangle Drawing Script

This script demonstrates basic OpenCV functionalities for editing images by adding text and drawing rectangles. Here’s a breakdown of what the script does:

Code Explanation

1. Reading the Image

image = cv2.imread('assignment-001-given.jpg')

This line loads the image file (assignment-001-given.jpg) from the current directory. Ensure the file exists in the same folder as the script.

2. Adding Text

cv2.putText(image, 
            'RAH972U',
            (830, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            3,
            (0, 255, 0),
            5,
            cv2.LINE_4)

Adds the text RAH972U at position (830, 180) using the FONT_HERSHEY_SIMPLEX font. The text is green ((0, 255, 0) in BGR format), with a font scale of 3 and a thickness of 5.

3. Drawing a Rectangle

cv2.rectangle(image, (250, 200), (980, 920), (0, 255, 0), 7)

Draws a green rectangle from the top-left corner (250, 200) to the bottom-right corner (980, 920). The thickness of the rectangle is 7 pixels.

4. Displaying the Image

cv2.namedWindow('Image window', cv2.WINDOW_NORMAL)
cv2.imshow('Image window', image)

Creates a resizable window titled Image window and displays the modified image.

5. Saving the Image

cv2.imwrite('result.jpg', image)

Saves the modified image as result.jpg in the current directory.

6. Closing the Window

cv2.destroyAllWindows()

Closes all OpenCV windows after any key is pressed.
