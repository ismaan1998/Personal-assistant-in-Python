from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text)
    tts.save('speech.mp3')
    playsound('speech.mp3')


