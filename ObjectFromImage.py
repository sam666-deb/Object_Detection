import cv2
import numpy as np
thrs = 0.45
img = cv2.imread('cat.jpg')

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
     classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

classIds, confs, bbox = net.detect(img, confThreshold=thrs)
print(classIds, bbox)
if len(classIds) != 0:
     for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
          cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
          cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
          cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 300, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

     cv2.imshow('Obejct Detector ', img)
     cv2.waitKey(0)