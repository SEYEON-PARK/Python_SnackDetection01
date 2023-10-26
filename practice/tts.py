import pyttsx3 # pyttsx3를 사용하기 위해
s = pyttsx3.init() 
data = "Sample Text" # 음성 파일로 만들 텍스트 문자열
s.say(data)  
s.runAndWait()  
