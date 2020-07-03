import speech_recognition as sr

# obtain audio from the microphone
def listen_to_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        
    try:
    
        return(r.recognize_google(audio))
    except sr.UnknownValueError:
        return("Google Speech Recognition could   not understand audio")
    except sr.RequestError as e:
        return("Could not request results from Google Speech Recognition service; {0}".format(e))