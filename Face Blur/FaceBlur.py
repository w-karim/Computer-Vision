import cv2
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
detector = FaceDetector(minDetectionCon = 0.75)

while True:
    _,frame = cap.read()
    frame, bboxs = detector.findFaces(frame, draw = False)
    
    if bboxs:
        for i,box in enumerate(bboxs):
            x,y,w,h = box['bbox']
            if x < 0 :
                x = 0
            if y < 0 :
                y = 0
            cropped_frame = frame[y : y + h, x : x + w]
            blurred_frame = cv2.blur(cropped_frame,(35,35))
            frame[y : y + h, x : x + w] = blurred_frame
            
    cv2.imshow("cap",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
