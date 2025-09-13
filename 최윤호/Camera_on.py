import cv2
from ultralytics import YOLO
import GrayMode as gm
import InvertMode as im
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

model = YOLO("yolov8n.pt")

def modeling(frame):
    re=model(frame)
    annotated_frame = re[0].plot()
    return annotated_frame

while 1:
    if(cv2.waitKey(1)==27): break
    ret, frame = capture.read()
    
    if(cv2.waitKey(1)==ord('g')):
        while 1:
            if(cv2.waitKey(1)==27): break
            ret, frame = capture.read()
            frame=gm.GreyMode(frame)
            cv2.imshow("Video",modeling(frame))
    if(cv2.waitKey(1)==ord('i')):
        while 1:
            if(cv2.waitKey(1)==27): break
            ret, frame = capture.read()
            frame=im.InvertMode(frame)
            cv2.imshow("Video",frame)
            re=model(frame)
            annotated_frame = re[0].plot()
            cv2.imshow("Video",modeling(frame))
    cv2.imshow("Video",modeling(frame))