import cv2
def GreyMode(frame):
    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    grayFrame = (r*0.299) + (g*0.587) + (b*0.114)
    grayFrame = grayFrame.astype('uint8')
    
    # 단일 채널 → 3채널 변환
    grayFrame = cv2.cvtColor(grayFrame, cv2.COLOR_GRAY2BGR)
    return grayFrame
