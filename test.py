import cv2
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    key = cv2.waitKey(1) & 0xff

    if not ret:
        break

    if key == ord('p'):
        print("KEy: ", key)
        while True:

            key2 = cv2.waitKey(1) or 0xff
            cv2.imshow('frame', frame)

            if key2 == ord('p'):
                break

    cv2.imshow('frame',frame)

    if key == 28: 
        break

cap.release()
cv2.destroyAllWindows()
