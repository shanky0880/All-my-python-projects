import cv2
from matplotlib import pyplot as plt


image = cv2.imread('WBC.jpg')
pic = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#cv2.imshow('original', image)
img = cv2.imread('WBC.jpg', 0)
#cv2.imshow('grey', img)

edged = cv2.Canny(img, 30, 200)
#cv2.imshow('edged image', edged)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

number = str(len(contours))

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.putText(image, 'Number of contours = ' + number, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#cv2.imshow('contours', image)

titles = ['original image', 'binary image', 'edged image', 'Contour']
images = [pic, img, edged, image]
for i in range(4):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()







