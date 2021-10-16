import cv2 as cv

img = cv.imread('Imagenes/Spider-Man_1.png')
cv.imshow('Spider', img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)

# Gaussins Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gauss)

# Medium Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)
