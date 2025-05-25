import os
from time import sleep
import time

from requests import get
import speech_recognition as sr
import eel

from .features import chatBot, closeCommands, findContact, makeCall, openCommands, playYoutube, whatsApp, sendMessage, get_ip
from .helper import is_running, speak, is_recycle_bin_empty, check_internet_speed
import webbrowser
import random
import psutil
import winshell
import sys
import instaloader
import wikipedia
import pyjokes

import pyautogui as pg



@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("Listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=10,phrase_time_limit=7)
        
    
    
    try:
        print("Recognizing.....")
        eel.DisplayMessage("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said {query}")

        eel.DisplayMessage(query)
        query = query.replace('jarvis','')
        query = query.replace('Jarvis','')
        print(query)
        # speak(query)
        
       

    except Exception as e: 
        return ''
    return query

@eel.expose
def allcommands(message=1):
    global task
    if message == 1:
        query = takecommand()
        query = query.lower()
        eel.senderText(query)
    else:
        query = message
        query = query.lower()
        eel.senderText(query)
        
    try:
        if "open" in query:
            openCommands(query) 
        elif "close" in query:
            closeCommands(query)
        elif "on youtube" in query:
            playYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query or "send sms" in query:
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("What mode to choose Whatsapp or Mobile")
                preference = takecommand()
                preference = preference.lower()
                print(preference)
                if 'whatsapp' in preference:
                    
                    flag = ""
                    if "send message" in query:
                        flag = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        flag = 'call'
                    else:
                        flag = 'video call'
                                        
                    whatsApp(contact_no, query, flag, name)
                    
                elif 'mobile' in preference:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
            else:
                speak("Contact not found")
                print("Contact not found")

        elif 'ip address' in query:
            speak("Checking IP Address Sir")
            ip = get_ip()
            print(f"Your IP Address is {ip}  ")
            speak(f"Your IP Address is {ip}  ")
        
        elif 'where i am' in query or 'where we are' in query or "location" in query:
            speak('Searching Location Sir')
            ip = get_ip()
            print(f"Your IP Address is {ip} Sir.... ")
            try:
                url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                geo = get(url)
                data = geo.json()

                city = data['city']
                country = data['country']
                print(f"I am not sure Sir but I think that we are in {city},{country}")
                speak(f"I am not sure Sir but I think that we are in {city},{country}")
            except:
                speak("Due to network issue I can't find the location")
        elif 'switch tab' in query:
            pg.keyDown('Alt')
            pg.press('Tab')
            speak("Switching tab Sir")
            pg.keyUp('Alt')

        elif 'screenshot' in query:
            speak("Tell the name of the screen shot file Sir")
            name = takecommand()
            speak("Hold on Sir.. I am taking screenshot..")
            time.sleep(3)
            img = pg.screenshot()
            img.save(f'images/{name}.png')
            print("Screen shot has been saved in the images folder Sir")
            speak("Screen shot has been saved in the images folder Sir")
        elif " shutdown" in query:
            speak("Shutting down Sir.... Goodbye!")
            time.sleep(3)
            os.system("shutdown /s /t 1")
        elif "restart" in query :
            speak("Restarting sir....")
            time.sleep(3)
            os.system("restart /r /t 1")
        elif "where is" in query:
            query = query.replace("where is","")
            location=query
            speak(f"Locating {location} Sir!....")
            time.sleep(2)
            webbrowser.open(f"https://google.co.in/maps/place/{location}")
        elif "wikipedia" in query:
            speak("Searching Wikipedia ")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak("According to Wikipedia, " + result)
        
        elif 'sleep' in query or 'exit' in query:
            print("Thanks for using me Sir....See you soon")
            speak("Thanks for using me Sir....See you soon")
            sys.exit()
        elif 'battery' in query :
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f'Sir our system has {percentage} percent battery')
            speak(f'Sir our system has {percentage} percent battery')
            if percentage >75:
                print("We have lot of power to do work")
                speak("We have lot of power to do work")
            elif percentage >50 and percentage <=75:
                print("We have enough power to do work")
                speak("We have enough power to do work")
            elif percentage > 20 and percentage <=50:
                print("We have low power Sir")
                speak("We have low power Sir")
            else:
                print("Power is too low Sir, we should charge")
                speak("Power is too low Sir, we should charge")
        elif "hide" in query or "visible" in query:
            speak("Do you want to hide the files or make the files visible?")
            chk = takecommand()
            if 'hide' in chk:
                os.system('attrib +h /s /d')
                speak("Sir ,All the files in the folder are hidden now")
            elif 'visible' in chk:
                os.system('attrib -h /s /d')
                speak("Sir ,All the files in the folder are visible now")
            elif 'leave' in chk:
                speak("Ok Sir!..")
        elif 'internet speed' in query or 'speed' in query:
            speak('Checking Internet Speed Sir')
        
        
            down, up = check_internet_speed()

            
            print(f"Download speed: {down / 1000000:.2f} Mbps")
            speak(f"Download speed: {down / 1000000:.2f} Mbps")
            
            
            print(f"Upload speed: {up / 1000000:.2f} Mbps")
            speak(f"Upload speed: {up / 1000000:.2f} Mbps")
            
        elif 'recycle' in query:
            if is_recycle_bin_empty():
                print("The Recycle Bin is already empty.")
                speak("The Recycle Bin is already empty.")
            else:
                speak('In progess Sir')
                winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
                print("Sir, Recycle bin has successfully emptied")
                speak("Sir, Recycle bin has successfully emptied")
        elif "tell me a joke" in query:
            speak("Here is a joke for you ")
            joke = pyjokes.get_joke(category="all")
            speak(joke)
            print(joke)
        elif "search on google" in query:
            speak("Sir, What do you want to search?")
            cm = takecommand()
            webbrowser.open(f"www.google.com/search?q={cm}")
        
            
        
        else:
            chatBot(query)
    except:
        eel.DisplayMessage("Sorry I didn't get it. Say it again")


    eel.ShowHood()    


