import cv2
from matplotlib import pyplot as plt
import joblib

img = cv2.imread('test_images/0 (236).jpg', 0)
#print(img.shape)
height,width = img.shape
plt.imshow(img,cmap='gray')

imgFlatten = img.reshape(height*width,1)
#print(imgFlatten.shape)

from sklearn.cluster import KMeans

model = KMeans(n_clusters=6)
model.fit(imgFlatten)
labels = model.labels_
#print(labels.shape)
labels2D = labels.reshape(height,width)

#plt.imshow(labels2D)
#plt.colorbar()
#plt.show()


#print(img[200:210,200:210])
#print('...........................................................')
#print(labels2D[200:210,200:210])


joblib.dump(model,"brain_tumor_Kmean.sav")

import cv2
import os
import joblib
import numpy as np




model = joblib.load('brain_tumor_Kmean.sav')
tumorLabel = 5

test_img_path = 'test_images'
test_img_names = os.listdir(test_img_path)

for test_img_name in test_img_names:
    img_path = os.path.join(test_img_path,test_img_name)

    img = cv2.imread(img_path,0)
    img_original = cv2.imread(img_path)

    height,width = img.shape
    imgFlatten = img.reshape(height*width,1)
    labels = model.predict(imgFlatten)
    labels2D = labels.reshape(height,width)
    mask = (labels2D == tumorLabel)
    tumorExtracted = np.bitwise_and(mask,img)
    contours,hiearachy = cv2.findContours(tumorExtracted,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    print('no. of contour:', len(contours))

    for index,cnt in enumerate(contours):
        area = cv2.contourArea(cnt)

        if(area > 1000):
            cv2.drawContours(img_original,[cnt],-1,(0,255,255),2)
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(img_original,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.rectangle(img_original,(x,y),(x+120,y-40),(0,255,0),-1)

            cv2.putText(img_original,'TUMOR',(x+10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255.255),2)

            cv2.imshow('Live',img_original)
            cv2.waitKey(1000)

        cv2.destroyAllWindows()