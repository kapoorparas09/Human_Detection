import cv2
cv2.__version__
import numpy as np
import torch
from matplotlib import pyplot as plt
# import matplotlib_inline
import winsound
import yaml

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
# model.conf = 0.6
# model.iou = 0.45
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    results = model(frame )
    # print(results)
    cv2.imshow('frame', np.squeeze(results.render()))

    if cv2.waitKey(1) & 0xFF == ord('q'): #Shutdown the camera by pressing Q
        break
    
cam.release()
cv2.destroyAllWindows()