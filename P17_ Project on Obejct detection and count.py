import cv2
import numpy as np

def nothing (x) :
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('WBC.jpg')

    Hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    L_H = cv2.getTrackbarPos("LH", "Tracking")
    L_S = cv2.getTrackbarPos("LS", "Tracking")
    L_V = cv2.getTrackbarPos("LV", "Tracking")

    U_H = cv2.getTrackbarPos("UH", "Tracking")
    U_S = cv2.getTrackbarPos("US", "Tracking")
    U_V = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([L_H, L_S, L_V])
    u_b = np.array([U_H, U_S, U_V])

    mask = cv2.inRange(Hsv, l_b, u_b)

    result = cv2.bitwise_or(frame, frame, mask=mask)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)

    edged = cv2.Canny(gray, L_S, U_S)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    number = str(len(contours))

    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv2.putText(frame, 'Number is = ' + number, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)




    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.imshow('edged image', edged)
    cv2.imshow('contours', frame)


    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

