import cv2
import numpy as np

def nothing (x) :
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    L_H = cv2.getTrackbarPos("LH", "Tracking")
    L_S = cv2.getTrackbarPos("LS", "Tracking")
    L_V = cv2.getTrackbarPos("LV", "Tracking")

    U_H = cv2.getTrackbarPos("UH", "Tracking")
    U_S = cv2.getTrackbarPos("US", "Tracking")
    U_V = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([L_H, L_S, L_V])
    u_b = np.array([U_H, U_S, U_V])

    mask = cv2.inRange(hsv, l_b, u_b)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

