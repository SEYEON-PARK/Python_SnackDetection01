# Import essential libraries
import requests
import cv2 # 영상처리를 하기 위해
import numpy as np
import imutils
import torch # 토치 추가
from gtts import gTTS # TTS 서비스를 위해 추가
from playsound import playsound # 음성 파일 나오게 하기 위해
import os
  
date =""
model = torch.hub.load('ultralytics/yolov5', 'custom', path='bestLast_final.pt')  # local model

blue_color=(255,0,0) # B, G, R 순서이다!

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.219.103:8080/shot.jpg" # 안드로이트 IP 웹캠을 사용하기 위해서
  
# While loop to continuously fetching data from the Url
while True: # 무한 반복
    frame_resp = requests.get(url)
    frame_arr = np.array(bytearray(frame_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(frame_arr, -1)
    #frame = imutils.resize(frame, width=640, height=640)
    #frame = cv2.resize(frame, dsize=(640,640), interpolation=cv2.INTER_AREA)

    results=model(frame) # 학습시킨 모델로 frame 분석한 결과를 results에 대입하기

    print(len(results.pandas().xyxy[0].xmin)) # 현재 탐지되는 객체의 개수 출력하기
    if(len(results.pandas().xyxy[0].xmin)>=2): # 만약, 탐지된 객체가 2개 이상이라면
        for i in range(len(results.pandas().xyxy[0].xmin)): # 탐지된 객체 수 만큼 반복
            print(results.pandas().xyxy[0].name[i])
            date="과자가 두 개 이상 잡혔습니다. 하나만 보여주세요." 
    else: # 만약, 탐지된 객체의 개수가 2개보다 작다면
        for i in range(len(results.pandas().xyxy[0].xmin)): # 탐지된 객체가 하나라도 있으면 반복(없으면 반복문을 돌지 않음. 만약, 이 문장이 없으면 객체가 탐지되지 않았을 때 잘못된 인덱스로 접근할 수 있음.)
            print(results.pandas().xyxy[0].name[i], results.pandas().xyxy[0].confidence[i]) # 탐지된 객체의 name과 confidence를 출력한다.(과자 이름, 몇 %로 확신했는지)
            if(results.pandas().xyxy[0].name[i]=="CornChips" and results.pandas().xyxy[0].confidence[i]>0.5): # 만약, 탐지된 객체의 name이 "CornChips"이고, confidence가 0.5 초과라면 
                date="콘칩입니다." # 콘칩임을 알려주는 텍스트 문자열
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3) # 사각형으로 객체 표시하기!
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2) # 텍스트도 표시하기!
            
            elif(results.pandas().xyxy[0].name[i]=="Gamjakkang" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="감자깡입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Kkobugchip" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="꼬북칩입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Kkulkkwabaegi" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="꿀꽈배기입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Koncho" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="콘초입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                
            elif(results.pandas().xyxy[0].name[i]=="Matdongsan" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="맛동산입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Ogamja" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="오감자입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                
            elif(results.pandas().xyxy[0].name[i]=="Pocachip_Onion" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="포카칩 어니언맛입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Postick" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="포스틱입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Saeukkang" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="새우깡입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
            elif(results.pandas().xyxy[0].name[i]=="Yangpaling" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="양파링입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

            elif(results.pandas().xyxy[0].name[i]=="konchi" and results.pandas().xyxy[0].confidence[i]>0.5):
                date="콘치입니다."
                frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
                cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            
    # Display the resulting frame
    cv2.imshow("Android_cam", frame) # frame 보여주기
    if(date!=""): # 만약, date가 빈 문자열이 아니라면
        tts = gTTS(text=date, lang='ko')
        tts.save("snack.mp3") # 음성 파일 저장하기
        playsound("snack.mp3") # 음성 파일 실행하기
        os.remove("snack.mp3") # 만든 파일은 바로 지우기!
        date="" # 해당 과자라는 메시지 말하는 거 한 번만 하게 하기 위해서 
	#   
	# 

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
  
cv2.destroyAllWindows()

'''
# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
  
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.219.107:8080/shot.jpg"
  
# While loop to continuously fetching data from the Url
while True:
    frame_resp = requests.get(url)
    frame_arr = np.array(bytearray(frame_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(frame_arr, -1)
    frame = imutils.resize(frame, width=1000, height=1800)
    cv2.imshow("Android_cam", frame)
  
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
  
cv2.destroyAllWindows()
'''
