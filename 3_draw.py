import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow("Blank", blank)

"""
# 1.  Paint the Image a certain colour
blank[100:200, 200:400] = 0, 0, 255
cv.imshow("RED", blank)


# 2. Draw a Rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=1)
cv.imshow("Rectangle", blank)


# 3. Draw a Circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 80, (0, 0, 255), thickness=1)
cv.imshow("Circle", blank)


# 4. Draw a Line

cv.line(blank, (100, 250), (300, 250), (0, 0, 255), thickness=5)
cv.imshow("Line", blank)

"""
# 5. Write Text
cv.putText(blank, "Hello", (0, 250), cv.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)
