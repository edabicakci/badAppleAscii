# import dependencies
import cv2
import math
import numpy as np
import time

# define standard width and height of an ascii character
charWidth = 10
charHeight = 10

# defines camera object with input from standard webcam
cam = cv2.VideoCapture("C:/Users/Matthew/Desktop/personalCode/pyCharm/BadApple.avi")

# checks if camera is successfully connected
if not cam.isOpened():
    raise IOError("Cannot Open video")

# ascii characters arranged by darkness from light on the left to dark on the right
asciiList = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
t1 = time.time()
# loop through frames
while True:

    # unpack tuple from camera input
    ret, inputFrame = cam.read()

    # if the frame can be grabbed that means the video is over
    if not ret:
        print("runtime:", time.time() - t1)
        raise IOError("Done!")

    # display original video
    cv2.imshow("original", inputFrame)

    # move original video out of the way
    cv2.moveWindow("original", 40, 30)

    # resize video to increase frame rate
    inputFrame = cv2.resize(inputFrame, (95, 62), interpolation=cv2.INTER_AREA)

    # creates a blank image
    blankFrame = np.zeros((len(inputFrame) * charWidth, len(inputFrame[0]) * charHeight, 3))

    # loop through image
    yCord = 0
    for line in inputFrame:
        xCord = 0
        for pixel in line:

            # grab color values
            r, g, b = pixel
            r = float(r)
            g = float(g)
            b = float(b)
            # get brightness of pixel
            brightness = (r + g + b) / 3

            # overlay ascii character based on brightness
            cv2.putText(blankFrame, asciiList[len(asciiList) - 1 - math.ceil(brightness / 4)],
                        (xCord, yCord), cv2.FONT_HERSHEY_PLAIN, 1, (1, 1, 1), 1)

            # increment by standard width
            xCord += charWidth

        # increment by standard height
        yCord += charHeight

    # display processed bad apple
    cv2.imshow("output", blankFrame)

    # move the window out of the way
    cv2.moveWindow("output", 600, 30)

    #  press escape to end program
    c = cv2.waitKey(1)
    if c == 27:
        break

# ends video capture
cam.release()

# closes the windows
cv2.destroyAllWindows()
