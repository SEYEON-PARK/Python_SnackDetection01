# import the opencv library
import cv2
import torch # 토치 추가
import numpy as np
from gtts import gTTS
from playsound import playsound
import os

date =""
model = torch.hub.load('ultralytics/yolov5', 'custom', path='snackBest04(200).pt')  # local model

# define a video capture object
vid = cv2.VideoCapture(0)

blue_color=(255,0,0)
count=0

while(True):
	img=np.zeros((1080, 1920, 3), np.uint8) # 빈 캔버스 만들기
	img=cv2.rectangle(img, (10, 10), (100, 100), blue_color, 3) # 제일 왼쪽 위에 꺼, 오른쪽 아래꺼
	
    
    # Capture the video frame
	# by frame
	ret, frame = vid.read()
	
	
	results=model(frame) # 만든 모델로 frame 분석!
	'''
	print(results.pandas().xyxy[0].to_json(orient="records"))
	print(results.pandas().xyxy[0].xmin)
	'''

	# (xmin, ymin)은 왼쪽 상단 좌표고, (xmax, ymax)는 오른쪽 하단 좌표다!
	print(len(results.pandas().xyxy[0].xmin))
	
	# 길이가 2 이상이라면 다른 메시지 추가!
	if(len(results.pandas().xyxy[0].xmin)>=2):
		date="과자가 두 개 이상 잡혔습니다. 하나만 보여주세요."
	else:
		for i in range(len(results.pandas().xyxy[0].xmin)):
			if(results.pandas().xyxy[0].name[i]=="Alsaeuchip" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="알새우칩입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Backside" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="뒷면입니다. 앞으로 돌려주세요."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="BananaKick" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="바나나킥입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="CaramelCornMaple" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="카라멜콘땅콩입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Cheetos" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="치토스입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="CornChips" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="콘칩입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Gamjakkang" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="감자깡입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Jjanggu" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="짱구입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="JollyPong" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="조리퐁입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Kkobugchip" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="꼬북칩입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Kkochgelang" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="꽃게랑입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Kkulkkwabaegi" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="꿀꽈배기입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="KokkalCorn" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="꼬깔콘입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Koncho" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="콘초입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Matdongsan" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="맛동산입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Ogamja" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="오감자입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Pocachip_Onion" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="포카칩 어니언맛입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Pocachip_Original" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="포카칩 오리지널맛입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Postick" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="포스틱입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Saeukkang" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="새우깡입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Sunchip" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="썬칩입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Swingchip" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="스윙칩입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
			elif(results.pandas().xyxy[0].name[i]=="Yangpaling" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="양파링입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

			elif(results.pandas().xyxy[0].name[i]=="konchi" and results.pandas().xyxy[0].confidence[i]>0.7):
				count+=1
				date="콘치입니다."
				frame=cv2.rectangle(frame, (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), (int(results.pandas().xyxy[0].xmax[i]), int(results.pandas().xyxy[0].ymax[i])), blue_color, 3)
				cv2.putText(frame, results.pandas().xyxy[0].name[i]+str(results.pandas().xyxy[0].confidence[i]), (int(results.pandas().xyxy[0].xmin[i]), int(results.pandas().xyxy[0].ymin[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
			
    # Display the resulting frame
	cv2.imshow('frame', frame)
	# print("count=", count)

	if(date!="" and count>=3):
		tts = gTTS(text=date, lang='ko')
		tts.save("snack.mp3")
		playsound("snack.mp3")
		os.remove("snack.mp3") # 만든 파일은 바로 지우기!
		date="" # 해당 과자라는 메시지 말하는 거 한 번만 하게 하기 위해서 
		count=0
	#   
	# 

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()