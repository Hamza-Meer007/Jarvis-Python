from time import sleep
import pyttsx3
import speech_recognition as sr
import eel


engine = pyttsx3.init('sapi5')
voice = engine.getProperty("voices")
engine.setProperty('voice',voice[0].id)


def speak(audio):
    audio = str(audio)
    engine.say(audio)
    eel.DisplayMessage(audio)()
    eel.receiverText(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("Listening....")()
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=10,phrase_time_limit=7)
        
    
    
    try:
        print("Recognizing.....")
        eel.DisplayMessage("Recognizing....")()
        query = r.recognize_google(audio,language="en-in")
        print(f"user said {query}")

        # eel.DisplayMessage(query)()
        query = query.replace('jarvis','')
        # speak(query)
        sleep(2)
       

    except Exception as e: 
        return ''
    return query.lower()