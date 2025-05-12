import speedtest
import win32com.client
import pywhatkit as kit
import winshell
from engine.command import *
import datetime,webbrowser,random
from requests import get
import time,os,pyjokes
import psutil
import pyautogui as pg
import instadownloader,instaloader
import wikipedia,sys
import eel


from speedtest import *
import pvporcupine
from hugchat.hugchat import ChatBot
import struct,pyaudio

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()












def chatBot(query):
    user_input = query.lower()
    chatbot = ChatBot(cookie_path="cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response



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










def wish():
    hour = int(datetime.datetime.now().hour)
    curr_time = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        print(f"Good Morning Sir......Its {curr_time}")
        speak(f"Good Morning Sir......Its {curr_time}")
    elif  hour>12 and hour <=18:
        print(f"Good Afternoon Sir......Its {curr_time}")
        speak(f"Good Afternoon Sir.....Its {curr_time}")
    else:
        print(f"Good Evening Sir......Its {curr_time}")
        speak(f"Good Evening Sir.....Its {curr_time}") 
    print("I am Jarvis Sir..... Please tell me how can I help You..?")
    speak("I am Jarvis Sir..... Please tell me how can I help You..?")
