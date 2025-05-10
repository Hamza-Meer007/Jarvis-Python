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








def is_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == task:
            return True
    return False

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

@eel.expose
def allcommands(message = 1):
    global task

    if message == 1:
        # wish()  
        loc = takecommand()
        eel.DisplayMessage(loc)
        query = loc.replace('jarvis','')
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        eel.DisplayMessage(query)

    
    try:
        if "open notepad" in query:
            speak("Opening Notepad ")
            path="C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
        elif "close notepad" in query:
            task = 'notepad.exe'
            if is_running():
                speak("closing notepad ")
                os.system('taskkill /f /im notepad.exe')
                
            else:
                speak("Notepad is already closed")
            
        elif "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
        elif "tell me a joke" in query:
            speak("Here is a joke for you ")
            joke = pyjokes.get_joke(category="all")
            speak(joke)
            print(joke)

        elif "open linkedin" in query:
            speak("Opening Linkedin ")
            webbrowser.open("www.Linkedin.com")

        elif "open cmd"  in query or "open command prompt" in query:
            speak("Opening cmd ")
            os.system('start cmd')
        elif "close command prompt" in query or 'close cmd' in query:
            task = 'cmd.exe'
            if is_running():
                speak("closing comand prompt")
                os.system('taskkill /f /im cmd.exe')
                
            else:
                speak("Comand prompt is already closed")
        elif "play music" in query:
            mus_dir = "C:\\Users\\ARMS\\Music\\songs"
            song= os.listdir(mus_dir)
            chk = random.choice(song)
            print(f"Playing song : {chk}")
            os.startfile(os.path.join(mus_dir,chk))
        elif "stop music" in query:
            task = 'vlc.exe'
            if is_running():
                speak("stopping music ")
                os.system('taskkill /f /im vlc.exe')
                
            else:
                speak("Music is already stopeed ")
        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            print(f"Your IP Address is {ip}  ")
            speak(f"Your IP Address is {ip}  ")

        elif "open facebook" in query:
            speak("Opening facebook ")
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            speak("Opening instagram ")
            webbrowser.open("www.instagram.com")

        elif "open stack overflow" in query:
            speak("Opening stack overflow ")
            webbrowser.open("www.stackoverflow.com")

        elif "search on google" in query:
            speak("Sir...... What do you want to search?")
            cm = takecommand()
            webbrowser.open(f"www.google.com/search?q={cm}")
        elif " shutdown" in query:
            speak("Shutting down Sir.... Goodbye!")
            time.sleep(3)
            os.system("shutdown /s /t 1")
        elif "restart" in query :
            speak("Restarting sir....")
            time.sleep(3)
            os.system("restart /r /t 1")
        elif 'set alarm' in query:
            speak("Tell the time Sir...")
            alarm = str(takecommand())
            alarm = alarm.split(":")
            print(alarm)
            timer1 = int(alarm[0])
            timer2 = int(alarm[1])
            speak("AM or PM....Sir!")
            timer3 = takecommand().upper()
            hour =  int(time.strftime("%I"))
            print(hour)
            min =  int(time.strftime("%M"))
            print(min)
            local = time.strftime("%p")
            print(local)
            if timer1 == hour and timer2 == min and timer3 == local:
                mus_dir = "C:\\Users\\ARMS\\Music\\songs"
                song= os.listdir(mus_dir)
                chk = random.choice(song)
                print(f"Playing song : {chk}")
                os.startfile(os.path.join(mus_dir,chk))
        elif "play song on youtube" in query:
            speak("Which song do you want to play?..Sir")
            search =takecommand()
            kit.playonyt(search)
            speak(f"playing {search} ")
        # elif "send whatsapp message" in query:
        # num = input("Write the number here (+92): ")
        # if num[0] == '0':
        #     num=num[1:]
        #     num = '+92'+num
        # elif num[0]=='+':
        #     num = num
        # else:
        #         print("you enter invalid number")
        #     # speak("Write the message Sir")
        #     # msg = input("Write your message :")
        #     # speak("Write the time in hour Sir")
        #     # hr = int(input("Write hour Sir: "))
        #     # speak("Write the time in minutes Sir ")
        #     # min = int(input("Write minutes Sir: "))
        #     # speak("Your message will be send shortly")
        #     # kit.sendwhatmsg(num,msg,hr,min)
        #     kit.sendwhatmsg("+923278797433","Hi Pumm kya hal hai",3,30)

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
            img.save(f'{name}.png')
            print("Screen shot has been saved in the main folder Sir.. You may check.")
            speak("Screen shot has been saved in the main folder Sir.. You may check.")

        elif 'where i am' in query or 'where we are' in query or "location" in query:
            speak('Searching Location Sir')
            ip = get("https://api.ipify.org").text
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
        
        elif 'check profile'in query or "check insta profile" in query:
            speak("Write the name of the profile Sir")
            id = input("Write the profile name: ")
            speak(f"Opening profile Sir")
            webbrowser.open(f"www.instagram.com/{id}")
            time.sleep(6)
            speak("Do you want to download the profile picture Sir")
            condition = takecommand()
            if 'yes' in condition:
                img = instaloader.Instaloader()
        
                img.download_profile(id,profile_pic_only=True)
                speak("Downloading Picture Sir!")
                time.sleep(3)
                speak("Picture has been downloaded in the main folder")
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
            speak("According to wikipedia" + result)
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
        elif 'sleep' in query or 'exit' in query:
            print("Thanks for using me Sir....See you soon")
            speak("Thanks for using me Sir....See you soon")
            sys.exit()
        elif 'battery' in query :
            battery = psutil.sensors_battery()
            percentage = battery.percent
            type(percentage)
            print(f'Sir our system has {percentage} percent battery')
            speak(f'Sir our system has {percentage} percent battery')
            if percentage >75:
                print("We have lot of power to do work")
                speak("We have lot of power to do work")
            elif percentage >50 or percentage <=75:
                print("We have enough power to do work")
                speak("We have enough power to do work")
            elif percentage > 20 or percentage <=50:
                print("We have low power Sir")
                speak("We have low power Sir")
            else:
                print("Power too low sir you should charge")
                speak("Power too low sir you should charge")

        elif 'internet speed' in query or 'speed' in query:
            speak('Checking Internet Speed Sir')
        
        
            download_speed, upload_speed = check_internet_speed()

            
            print(f"Download speed: {results['download'] / 1000000:.2f} Mbps")
            speak(f"Download speed: {results['download'] / 1000000:.2f} Mbps")
            
            
            print(f"Upload speed: {results['upload'] / 1000000:.2f} Mbps")
            speak(f"Upload speed: {results['upload'] / 1000000:.2f} Mbps")
            
        elif 'recycle' in query:
            if is_recycle_bin_empty():
                print("The Recycle Bin is already empty.")
                speak("The Recycle Bin is already empty.")
            else:
                speak('In progess Sir')
                winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
                print("Sir, Recycle bin has successfully emptied")
                speak("Sir, Recycle bin has successfully emptied")
        elif 'volume up' in query:
            pg.press('volume up')
            speak('Done Sir')
            
        elif 'volume down' in query:
            pg.press('volume down')
            speak('Done Sir')

        elif 'volume mute' in query or 'mute' in query:
            pg.press('volume mute')
            speak('Done Sir')
        
        elif 'volume full' in query:
            for x in range(50):
                pg.press('volumeup')
                sleep(0.1) 
            speak('Done Sir')

        else:
            res = chatBot(query)
            eel.DisplayMessage(res)()  

    except:
        eel.DisplayMessage('Say it again Sir')
    
    eel.ShowHood()()

