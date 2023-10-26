import pyttsx3 # pyttsx3를 사용하기 위해
s = pyttsx3.init() 
data = "Sample Text"  
s.say(data)  
s.runAndWait()  
