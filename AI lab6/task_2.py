import cv2

classNames = []
file_name = 'Labels.txt'
with open(file_name, 'rt') as fpt:
    classNames = fpt.read().rstrip('\n').split('\n')

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model, config_file)

model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

cap = cv2.VideoCapture(0) # Use 0 for webcam, or replace with video file path

cv2.namedWindow("Webcam Output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam Output", 800, 600)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    classIds, confs, bbox = model.detect(frame, confThreshold=0.55)

    if len(classIds) != 0:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            if 0 < classId <= len(classNames):
                label = f'{classNames[classId - 1]}: {round(conf * 100)}%'
                cv2.rectangle(frame, box, (0, 255, 0), thickness= 2)
                cv2.putText(frame, label, (box[0] + 10, box[1] + 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam Output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
