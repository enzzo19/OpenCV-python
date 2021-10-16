import cv2 as cv


def rescaleFrame(frame, scale=0.2):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

"""
img = cv.imread('Imagenes/Spider-Man_1.png')
img_resize = rescaleFrame(img)
cv.imshow('Image', img)
cv.imshow("Image Resized", img_resize)
cv.waitKey(0)


"""
# Reading Videos
capture = cv.VideoCapture("Videos/Spider-Man-3.mp4")  # Reference WEBCAM

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

