import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random
  
  
rock = cv2.imread("C:/Users/kwarg/OneDrive/Bureau/rock2.png", cv2.IMREAD_UNCHANGED)
paper = cv2.imread("C:/Users/kwarg/OneDrive/Bureau/paper2.png",cv2.IMREAD_UNCHANGED)
scissor = cv2.imread("C:/Users/kwarg/OneDrive/Bureau/scissor2.png",cv2.IMREAD_UNCHANGED)
Possible_plays = [rock,paper,scissor]
background_image = cv2.imread("C:/Users/kwarg/OneDrive/Bureau/background_image.png")

vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
window_name ="Rock Paper Scissor"

Hand_detector = HandDetector(maxHands = 1)

Timer = 0
Reset_timer = False
GameStart = False
Countdown = False
hands = False
font = cv2.FONT_HERSHEY_PLAIN

whitecolor = (255,255,255)
redcolor = (255,0,0)
blackcolor = (0,0,0)

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (0,0), None, 0.77 , 0.77)
    frame = frame[:,13:413]
    hands,img = Hand_detector.findHands(frame)
    background_image[156:526,592:992] = frame
    if GameStart:
        if Countdown is False:
            Timer = time.time() - TimeStart
            if Timer > 1:
                cv2.putText(background_image, "Get ready", (460,580), font, 2, blackcolor, 2)

            if Timer > 3 :
                cv2.putText(background_image, "Get ready", (460,580), font, 2, whitecolor, 2)
                cv2.putText(background_image, str(int(Timer)), (537,330), font, 2, blackcolor, 2)
                
            if Timer > 4:
                cv2.putText(background_image, "3", (537,330), font, 2, whitecolor, 2)
                cv2.putText(background_image, "4", (537,330), font, 2, whitecolor, 2)
                cv2.putText(background_image, "Go", (530,580), font, 2, blackcolor, 2)
            
            if Timer > 5:
                cv2.putText(background_image, "5", (537,330), font, 2, blackcolor, 2)
                cv2.putText(background_image, "5", (537,330), font, 2, whitecolor, 2)
                cv2.putText(background_image, "Go", (530,580), font, 2, whitecolor, 2)
                Countdown = True
                Timer = 0

                if hands:
                    hand = hands[0]
                    fingers = Hand_detector.fingersUp(hand)
                    if fingers == [0,0,0,0,0]:
                        result = "rock"
                    if fingers == [1,1,1,1,1]:
                        result = "paper"
                    if fingers == [0,1,1,0,0]:
                        result = "scissor"
                    print(result, fingers)
                    r = random.randint(0,2)
                    Possible_plays[r] = cv2.resize(Possible_plays[r], (400,371))
                    background_image = cvzone.overlayPNG(background_image,Possible_plays[r],(107,156))
                    cv2.imshow(window_name, background_image)
                    if (result == "paper" and r == 0) or (result == "scissor" and r == 1) or (result == "rock" and r == 2):
                        cv2.putText(background_image, "Player win !", (700,560), font, 2, blackcolor, 2)
                    elif (result == "rock" and r == 0) or (result == "paper" and r == 1) or (result == "scissor" and r == 2):
                        cv2.putText(background_image, "Tie !", (700,560), font, 2, blackcolor, 2)
                        cv2.putText(background_image, "Tie !", (220,560), font, 2, blackcolor, 2)
                    else : 
                        cv2.putText(background_image, "AI win !", (220,560), font, 2, blackcolor, 2)
    cv2.imshow(window_name, background_image)
    pressed_key = cv2.waitKey(1)  
    if pressed_key == ord('q'):
        break
    elif pressed_key == ord('s'):
        GameStart = True
        TimeStart = time.time()
        Countdown = False
        cv2.putText(background_image, "Player win !", (700,560), font, 2, whitecolor, 2)
        cv2.putText(background_image, "Tie !", (700,560), font, 2, whitecolor, 2)
        cv2.putText(background_image, "Tie !", (220,560), font, 2, whitecolor, 2)
        cv2.putText(background_image, "AI win !", (220,560), font, 2, whitecolor, 2)
        
vid.release()
cv2.destroyAllWindows()



