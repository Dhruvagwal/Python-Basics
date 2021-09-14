import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    print(frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
