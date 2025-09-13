
def GreyMode(frame):
    b=frame[:,:,0]
    g=frame[:,:,1]
    r=frame[:,:,2]
    grayFrame=(r*0.299)+(g*0.587)+(b*0.114)
    grayFrame=grayFrame.astype('uint8')

    return grayFrame
    