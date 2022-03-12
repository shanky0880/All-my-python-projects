import cv2
import numpy as np


img = cv2.imread('WBC.jpg')
needle_img = cv2.imread('WBC crop image.jpg')

result = cv2.matchTemplate(img,needle_img,cv2.TM_CCOEFF_NORMED)


threshold = 0.7
locations = np.where(result>=threshold)
locations = list(zip(*locations[::-1]))
print(locations)
if locations:

    print('Found needle')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    for loc in locations:

        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        image = cv2.rectangle(img,top_left,bottom_right,(0,255,0),1,cv2.LINE_4 )
        cv2.putText(image, 'Cancer cell ', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Result', image )
    cv2.waitKey()
else:
    print("needle not found")

