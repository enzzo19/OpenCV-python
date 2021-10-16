import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# img = cv.imread('Imagenes/images_letters_2.jpg')
img = cv.imread('Imagenes/Spider-Man_2.png')
cv.imshow('Spider', img)

blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[1] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Mask", masked)
"""
# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
"""

# Colour Histogram

plt.figure()
plt.title("Colours Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
cv.waitKey(0)
