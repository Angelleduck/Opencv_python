import cv2
# connecting the webcam
cap=cv2.VideoCapture(0)

# loading cascade

cascade=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
# cascade=cv2.CascadeClassifier('haarcascades\haarcascade_eye.xml')

# reading frames 
while True:
    ret,frame=cap.read()
    
    # implementing detection
    corner=cascade.detectMultiScale(frame,scaleFactor=1.2)
    for(x,y,w,h)in corner:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,200,250),5)

    # displaying widow
    cv2.imshow('window',frame)

    # close
    if(cv2.waitKey(1)==ord('q')):
        break

