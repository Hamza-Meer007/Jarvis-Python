
import pywhatkit as kit
import winshell
from engine.command import *
import datetime,webbrowser,random
from requests import get
import time,os,pyjokes
import psutil

import instadownloader,instaloader
import wikipedia,sys
import eel


from speedtest import *
import pvporcupine

import struct,pyaudio
































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
