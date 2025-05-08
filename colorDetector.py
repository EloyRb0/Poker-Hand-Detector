import cv2
import numpy as np


def detectColor(figure):

    #HSV scale convertor
    hsv = cv2.cvtColor(figure, cv2.COLOR_BGR2HSV)

    #RedMask
    lowRed1 = np.array([0, 100, 100])
    highRed1 = np.array([10, 255, 255])
    lowRed2 = np.array([160, 100, 100])
    highRed2 = np.array([179, 255, 255])
    redMask = cv2.inRange(hsv, lowRed1, highRed1) + cv2.inRange(hsv, lowRed2, highRed2)

    #Black Mask
    lowBlack = np.array([0, 0, 0])
    highBlack = np.array([180, 255, 50])
    blackMask = cv2.inRange(hsv, lowBlack, highBlack)

    #Counts pixels on each mask
    RedPixels = cv2.countNonZero(redMask)
    blackPixels = cv2.countNonZero(blackMask)

    #Returns 1 if figure is red, otherwise return black
    if RedPixels > blackPixels:
        return 1
    else:
        return 0