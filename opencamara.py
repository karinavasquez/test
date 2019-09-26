import numpy as np
import cv2

cap = cv2.VideoCapture(0)
kernel = np.ones((3,3),np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #canny = cv2.Canny(gray,100,350)
    ret,thresh2 = cv2.threshold(frame,127,255,0)
    #closing = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel)

    image, contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[4]
    salida = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)
   
    # Display the resulting frame
    cv2.imshow('frame',salida)
    cv2.imshow('thresh2', thresh2)
    cv2.imshow('canny',canny)
    print (contours)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()