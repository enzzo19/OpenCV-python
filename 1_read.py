# Import library
import cv2 as cv
"""
# Read Image
img = cv.imread('Imagenes/Spider-Man_1.png')

cv.imshow('Spider', img)

cv.waitKey(0)
"""
# Reading Videos
capture = cv.VideoCapture("Videos/Spider-Man-3.mp4")  # Reference WEBCAM

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
