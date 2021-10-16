import cv2 as cv
import numpy as np

img = cv.imread('Imagenes/Spider-Man_3.png')
cv.imshow('Spider', img)

# Translation

"""
def translate(img, x, y):

    # -x --> left
    # -y --> up
    # x --> rigth
    # y --> down

    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 0, 0)
cv.imshow("Translate", translated)
print("Tamaño TRASLATE: ", str(translated.shape))

"""
# Rotation
def rotating(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotating(img, 180)
cv.imshow("Rotated", rotated)

rotated_rotated = rotating(img, 90)
cv.imshow("Rotate Rotate", rotated_rotated)


"""
# Resizing
resized = cv.resize(img, (200, 200), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow("Flip", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)
"""

cv.waitKey(0)
