import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 500)
cap.set(4, 500)
print(cap.get(3))
print(cap.get(4))


while (cap.isOpened()):
    ret, img = cap.read()

    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width :' + str(cap.get(3)) + 'Height :' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        img = cv2.putText(img, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA )

        cv2.imshow("video", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()