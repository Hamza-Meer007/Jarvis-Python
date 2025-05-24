import re
import psutil
import pyttsx3
import eel
import os
import time
import speedtest
import win32com.client

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty("voices")
    engine.setProperty('voice',voice[0].id)
    engine.setProperty('rate',174)
    audio = str(audio)
    engine.say(audio)
    eel.DisplayMessage(audio)
    eel.receiverText(audio)   
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

def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string




# key events like receive call, stop call, go back
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')


def is_recycle_bin_empty():
    shl = win32com.client.Dispatch("Shell.Application")
    recycle_bin = shl.NameSpace(10)  # 10 corresponds to the Recycle Bin
    items = recycle_bin.Items()

    return items.Count == 0

def check_internet_speed():
    global results
    st = speedtest()
    down = st.download()
    up = st.upload()
    st.results.share()
    results = st.results.dict()

    return down,up