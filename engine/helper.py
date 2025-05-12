import re
import psutil
import pyttsx3
import eel

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty("voices")
    engine.setProperty('voice',voice[0].id)
    engine.setProperty('rate',174)
    audio = str(audio)
    engine.say(audio)
    eel.DisplayMessage(audio)
    # eel.receiverText(audio)
    engine.runAndWait()
    
def is_running():
    global task
    for process in psutil.process_iter(['name']):
        if process.info['name'] == task:
            return True
    return False

    
def extract_yt_term(command):
    # Updated regex to handle more variations
    pattern = r'play\s+(.*?)\s+(on\s+youtube|on\s+YouTube|on\s+yt)'
    match = re.search(pattern, command, re.IGNORECASE)
    
    return match.group(1) if match else None