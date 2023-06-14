print("Human Detection")

import cv2
print(cv2.__version__)
cascade_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade_fullbody = cv2.CascadeClassifier("haarcascade_fullbody.xml")
cascade_upperbody= cv2.CascadeClassifier("haarcascade_upperbody.xml")
cascade_lowerbody = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
cascade_hand = cv2.CascadeClassifier("hand.xml")
cascade_fist = cv2.CascadeClassifier("fist.xml")
cascade_palm = cv2.CascadeClassifier("palm.xml")


cam = cv2.VideoCapture(0)

def face():
    f = cascade_face.detectMultiScale(con)

    for (x,y,w,h) in f:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

def fullbody():
    fb = cascade_fullbody.detectMultiScale(con)

    for (x,y,w,h) in fb:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

def upperbody():
    ub = cascade_upperbody.detectMultiScale(con)

    for (x,y,w,h) in ub:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

def hand():
    hand = cascade_hand.detectMultiScale(con)

    for (x,y,w,h) in hand:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

def fist():
    fist = cascade_fist.detectMultiScale(con)

    for (x,y,w,h) in fist:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

def palm():
    palm = cascade_palm.detectMultiScale(con)

    for (x,y,w,h) in palm:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

def lowerbody():
    lb = cascade_lowerbody.detectMultiScale(con)

    for (x,y,w,h) in lb:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)

while True:
    ret , frame = cam.read()
    con = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face()
    fullbody()
    upperbody()
    lowerbody()
    hand()
    fist()
    palm()
    lowerbody()

    cv2.imshow('img', frame)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()