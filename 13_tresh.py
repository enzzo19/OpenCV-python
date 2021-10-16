import cv2 as cv

# img = cv.imread('Imagenes/images_letters_2.jpg')
img = cv.imread('Imagenes/Spider-Man_2.png')
cv.imshow('Spider', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple Tresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Tresholding", thresh)

# Inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Tresholding_inverse", thresh_inv)


# Adaptative Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive", adaptive_thresh)



cv.waitKey(0)
