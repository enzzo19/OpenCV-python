import cv2 as cv

img = cv.imread('Imagenes/Spider-Man_2.png')
print("Img: ", str(img.shape))
cv.imshow('Spider', img)

# Basics Functions
"""
# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)


# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)


# Dilating the Image
dilated = cv.dilate(canny, (3, 3), iterations=2)
cv.imshow('Dilated', dilated)


# Eroding
eroded = cv.erode(img, (3, 3), iterations=10)
cv.imshow("Eroded", eroded)

"""

# Resize
resize = cv.resize(img, (250, 600), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resize)

# Cropping
cropped = img[100:300, 300:450]
cv.imshow("Cropped", cropped)
print("Croped: ", cropped.shape)

cv.waitKey(0)
