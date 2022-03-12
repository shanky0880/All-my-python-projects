import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())


while (cap.isOpened()):
    ret, img = cap.read()

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()