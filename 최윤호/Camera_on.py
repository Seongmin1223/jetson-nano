import cv2
from ultralytics import YOLO
import GrayMode as gm
import InvertMode as im

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

model = YOLO("yolov8n.pt")

def modeling(frame):
    re = model(frame)
    annotated_frame = re[0].plot()
    return annotated_frame

mode = "normal"  # 현재 모드 저장 변수

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # 현재 모드에 따라 전처리
    if mode == "gray":
        frame = gm.GreyMode(frame)
    elif mode == "invert":
        frame = im.InvertMode(frame)

    # YOLO 적용 후 출력
    cv2.imshow("Video", modeling(frame))

    key = cv2.waitKey(1) & 0xFF
    if key == 27:   # ESC 종료
        break
    elif key == ord('g'):
        mode = "gray"
    elif key == ord('i'):
        mode = "invert"
    elif key == ord('n'):
        mode = "normal"   # 원본 모드 복귀
