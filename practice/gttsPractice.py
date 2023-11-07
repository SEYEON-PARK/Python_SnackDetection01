from gtts import gTTS # 구글에서 제공하는 TTS 서비스를 이용하기 위해
from playsound import playsound # 음성 파일을 재생하기 위해

text ="재밌게 놀아!"

tts = gTTS(text=text, lang='ko')
tts.save("hello.mp3")
playsound("hello.mp3")

