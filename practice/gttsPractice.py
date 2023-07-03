from gtts import gTTS
from playsound import playsound

text ="재밌게 놀아!"

tts = gTTS(text=text, lang='ko')
tts.save("hello.mp3")
playsound("hello.mp3")

