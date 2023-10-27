import pyttsx3 # pyttsx3를 사용하기 위해
s = pyttsx3.init() 
data = "Sample Text" # 음성 파일로 만들 텍스트 문자열 data
s.say(data) # 텍스트 문자열 말하게 하기!(음성 출력)
s.runAndWait() # 음성 출력이 완료될 때까지 대기
