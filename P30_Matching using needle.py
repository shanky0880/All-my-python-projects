import cv2
import numpy as np


img = cv2.imread('WBC.jpg')
needle_img = cv2.imread('WBC crop image.jpg')

result = cv2.matchTemplate(img,needle_img,cv2.TM_CCOEFF_NORMED)

min_val , max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print("Best match top left %s" % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('found needle')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    image = cv2.rectangle(img,top_left,bottom_right,(0,255,0),2,cv2.LINE_4 )

    cv2.imshow('Result', image)
    cv2.waitKey()
else:
    print("needle not found")

