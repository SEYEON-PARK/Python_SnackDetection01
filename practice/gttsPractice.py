from gtts import gTTS # 구글에서 제공하는 TTS 서비스를 이용하기 위해
from playsound import playsound # 음성 파일을 재생하기 위해

text ="재밌게 놀아!" # 텍스트 문자열

tts = gTTS(text=text, lang='ko') # gTTS 객체 tts 만들기!
tts.save("hello.mp3") # 음성 파일 저장하기
playsound("hello.mp3") # 음성 파일 실행하기

