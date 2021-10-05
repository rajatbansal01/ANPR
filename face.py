import cv2
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def detect(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #changing RGB to gray for better classification
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is not ():
        for (x,y,w,h) in faces:
            cv2.rectangle(frame ,(x-w//2,y-h//2), (x+2*w ,y+2*h),(255,0,0),2)
            img = frame[y-h//2:y+2*h , x-w//2:x+2*w]
        return(img)
    else:
        return(frame)

#face.py
cap_face = cv2.VideoCapture(0)
while cap_face.isOpened():
    #time.sleep(0.2)
    ret,frame = cap_face.read()
    if ret:
        face_image = detect(frame)
        cv2.imshow("video" , face_image)
        if cv2.waitKey(1) & 0xFF == ord('q'): # press enter and "q" key to close the window
            break
    else:
        break
cap_face.release()
cv2.destroyAllWindows()