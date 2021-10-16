import cv2 as cv
import numpy as np

img = cv.imread('Imagenes/Spider-Man_1.png')
cv.imshow('Spider', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("BLUE", blue)
cv.imshow("GREEN", green)
cv.imshow("RED", red)

print(img.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

merged_image = cv.merge([b, g, r])
cv.imshow("Merge Image", merged_image)

cv.waitKey(0)
