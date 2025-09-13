def InvertMode(frame):
    b=frame[:,:,0]
    g=frame[:,:,1]
    r=frame[:,:,2]
    invertFrame=225-frame

    return invertFrame