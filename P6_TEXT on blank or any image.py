import numpy as np

import cv2
img = cv2.imread('lena.jpg')
#img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (0, 255, 255), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (0, 255, 255), 5)

img = cv2.rectangle(img, (384, 0), (510,128), (0, 255, 255), 5)

img = cv2.circle(img, (350,70), 65, (0, 255, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img, 'OPENCV', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)


cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()