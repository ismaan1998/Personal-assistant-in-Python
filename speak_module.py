import pyttsx3

def speak (usertext):
    engine = pyttsx3.init()
    engine.say(usertext)
    engine.runAndWait()




