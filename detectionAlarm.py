import cv2
import winsound
import imutils
import threading
cascade_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade_fullbody = cv2.CascadeClassifier("haarcascade_fullbody.xml")
# cascade_upperbody= cv2.CascadeClassifier("haarcascade_upperbody.xml")
cascade_lowerbody = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
cascade_hand = cv2.CascadeClassifier("hand.xml")
# cascade_fist = cv2.CascadeClassifier("fist.xml")
# cascade_palm = cv2.CascadeClassifier("palm.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ret, frame1 = cap.read()
frame1 = imutils.resize(frame1, width=500)
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21,21),0)

alarm = False
alarm_mode = False
alarm_counter = 0


def face():
    f = cascade_face.detectMultiScale(con)

    for (x,y,w,h) in f:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
        beep_alarm()

def fullbody():
    fb = cascade_fullbody.detectMultiScale(con)

    for (x,y,w,h) in fb:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
        beep_alarm()

# def upperbody():
#     ub = cascade_upperbody.detectMultiScale(con)

#     for (x,y,w,h) in ub:
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
#         beep_alarm()


def hand():
    hand = cascade_hand.detectMultiScale(con)

    for (x,y,w,h) in hand:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
        beep_alarm()


# def fist():
#     fist = cascade_fist.detectMultiScale(con)

#     for (x,y,w,h) in fist:
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
#         beep_alarm()


# def palm():
#     palm = cascade_palm.detectMultiScale(con)

#     for (x,y,w,h) in palm:
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
#         beep_alarm()


def lowerbody():
    lb = cascade_lowerbody.detectMultiScale(con)

    for (x,y,w,h) in lb:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
        beep_alarm()


def beep_alarm():
    global alarm
    for _ in range(1):
        if not alarm_mode:
            break
        print("Alarm")
        winsound.Beep(2500, 2000)
    alarm = False

while True:
    ret , frame = cap.read()
    frame = imutils.resize(frame, width=500)

    con = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face()
    fullbody()
    # upperbody()
    lowerbody()
    hand()
    # fist()
    # palm()
    # lowerbody()

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5,5),0)

        difference = cv2.absdiff(frame_bw, frame1)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        frame1 = frame_bw

        if threshold.sum()> 500:
            alarm_counter += 1
        else:
            if alarm_counter >0:
                alarm_counter -=1

        cv2.imshow("Cam", threshold)
        cv2.imshow("Cam", frame)

    else:
        cv2.imshow("Cam", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()
    
    key_pressed = cv2.waitKey(30)
    # if key_pressed == ord("t"):
    alarm_mode = not alarm_mode
    alarm_counter = 0

    if key_pressed == ord("q"):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()