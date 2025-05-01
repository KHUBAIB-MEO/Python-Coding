import cv2

img = cv2.imread('images/kids.png')
classNames = []
file_name = 'Labels.txt'

with open(file_name, 'rt') as fpt:
    classNames = fpt.read().rstrip('\n').split('\n')

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)
       
model.setInputSize(320, 320) 
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)
cap = cv2.VideoCapture('videos/kids.mp4')

classIds, confs, bbox = model.detect(img, confThreshold=0.55) 

for classId, confidece, box in zip(classIds.flatten(), confs.flatten(), bbox):
    cv2.rectangle(img, box, (0, 255, 0), thickness = 1)
    cv2.putText(img, classNames[classId - 1],(box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)   



cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Output", 800, 600)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

