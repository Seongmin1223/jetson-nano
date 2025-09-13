import cv2
import GrayMode as gm
import InvertMode as im
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

while 1:
    if(cv2.waitKey(1)==27): break
    ret, frame = capture.read()
    if(cv2.waitKey(1)==ord('g')):
        while 1:
            if(cv2.waitKey(1)==27): break
            ret, frame = capture.read()
            frame=gm.GreyMode(frame)
            cv2.imshow("Video",frame)
    if(cv2.waitKey(1)==ord('i')):
        while 1:
            if(cv2.waitKey(1)==27): break
            ret, frame = capture.read()
            frame=im.InvertMode(frame)
            cv2.imshow("Video",frame)
    cv2.imshow("Video",frame)