import cv2

face_cascade = cv2.CascadeClassifier("cascade.xml")

#img = cv2.imread('elon2.jpg')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.02, 1)
    for(x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.putText(img, 'Elon face', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
