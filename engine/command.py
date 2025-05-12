import os
from time import sleep

import speech_recognition as sr
import eel

from .features import closeCommands, openCommands, playYoutube
from .helper import is_running, speak






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
def allcommands():
    global task
    try:
        query = takecommand()
        query = query.lower()
        if "open" in query:
            openCommands(query) 
        elif "close" in query:
            closeCommands(query)
        elif "on youtube" in query:
            playYoutube(query)
        
        else:
            pass
    except Exception as e:
        print(f"Error: {e}")


    eel.ShowHood()    
# @eel.expose
# def allcommands(message = 1):
#     global task

#     if message == 1:
#         # wish()  
#         loc = takecommand()
#         eel.DisplayMessage(loc)
#         query = loc.replace('jarvis','')
#         eel.senderText(query)
#     else:
#         query = message
#         eel.senderText(query)
#         eel.DisplayMessage(query)

    
#     try:
#         
                
#             
            
#         elif "open youtube" in query:
#             speak("Opening Youtube ")
#             webbrowser.open("www.youtube.com")
#         elif "open google" in query:
#             speak("Opening Google ")
#             webbrowser.open("www.google.com")
#         elif "tell me a joke" in query:
#             speak("Here is a joke for you ")
#             joke = pyjokes.get_joke(category="all")
#             speak(joke)
#             print(joke)

#         elif "open linkedin" in query:
#             speak("Opening Linkedin ")
#             webbrowser.open("www.Linkedin.com")

#         elif "open cmd"  in query or "open command prompt" in query:
#             speak("Opening cmd ")
#             os.system('start cmd')
#         elif "close command prompt" in query or 'close cmd' in query:
#             task = 'cmd.exe'
#             if is_running():
#                 speak("closing comand prompt")
#                 os.system('taskkill /f /im cmd.exe')
                
#             else:
#                 speak("Comand prompt is already closed")
#         elif "play music" in query:
#             mus_dir = "C:\\Users\\ARMS\\Music\\songs"
#             song= os.listdir(mus_dir)
#             chk = random.choice(song)
#             print(f"Playing song : {chk}")
#             os.startfile(os.path.join(mus_dir,chk))
#         elif "stop music" in query:
#             task = 'vlc.exe'
#             if is_running():
#                 speak("stopping music ")
#                 os.system('taskkill /f /im vlc.exe')
                
#             else:
#                 speak("Music is already stopeed ")
#         elif 'ip address' in query:
#             ip = get("https://api.ipify.org").text
#             print(f"Your IP Address is {ip}  ")
#             speak(f"Your IP Address is {ip}  ")

#         elif "open facebook" in query:
#             speak("Opening facebook ")
#             webbrowser.open("www.facebook.com")

#         elif "open instagram" in query:
#             speak("Opening instagram ")
#             webbrowser.open("www.instagram.com")

#         elif "open stack overflow" in query:
#             speak("Opening stack overflow ")
#             webbrowser.open("www.stackoverflow.com")

#         elif "search on google" in query:
#             speak("Sir...... What do you want to search?")
#             cm = takecommand()
#             webbrowser.open(f"www.google.com/search?q={cm}")
#         elif " shutdown" in query:
#             speak("Shutting down Sir.... Goodbye!")
#             time.sleep(3)
#             os.system("shutdown /s /t 1")
#         elif "restart" in query :
#             speak("Restarting sir....")
#             time.sleep(3)
#             os.system("restart /r /t 1")
#         elif 'set alarm' in query:
#             speak("Tell the time Sir...")
#             alarm = str(takecommand())
#             alarm = alarm.split(":")
#             print(alarm)
#             timer1 = int(alarm[0])
#             timer2 = int(alarm[1])
#             speak("AM or PM....Sir!")
#             timer3 = takecommand().upper()
#             hour =  int(time.strftime("%I"))
#             print(hour)
#             min =  int(time.strftime("%M"))
#             print(min)
#             local = time.strftime("%p")
#             print(local)
#             if timer1 == hour and timer2 == min and timer3 == local:
#                 mus_dir = "C:\\Users\\ARMS\\Music\\songs"
#                 song= os.listdir(mus_dir)
#                 chk = random.choice(song)
#                 print(f"Playing song : {chk}")
#                 os.startfile(os.path.join(mus_dir,chk))
#         elif "play song on youtube" in query:
#             speak("Which song do you want to play?..Sir")
#             search =takecommand()
#             kit.playonyt(search)
#             speak(f"playing {search} ")
#         # elif "send whatsapp message" in query:
#         # num = input("Write the number here (+92): ")
#         # if num[0] == '0':
#         #     num=num[1:]
#         #     num = '+92'+num
#         # elif num[0]=='+':
#         #     num = num
#         # else:
#         #         print("you enter invalid number")
#         #     # speak("Write the message Sir")
#         #     # msg = input("Write your message :")
#         #     # speak("Write the time in hour Sir")
#         #     # hr = int(input("Write hour Sir: "))
#         #     # speak("Write the time in minutes Sir ")
#         #     # min = int(input("Write minutes Sir: "))
#         #     # speak("Your message will be send shortly")
#         #     # kit.sendwhatmsg(num,msg,hr,min)
#         #     kit.sendwhatmsg("+923278797433","Hi Pumm kya hal hai",3,30)

#         elif 'switch tab' in query:
#             pg.keyDown('Alt')
#             pg.press('Tab')
#             speak("Switching tab Sir")
#             pg.keyUp('Alt')

#         elif 'screenshot' in query:
#             speak("Tell the name of the screen shot file Sir")
#             name = takecommand()
#             speak("Hold on Sir.. I am taking screenshot..")
#             time.sleep(3)
#             img = pg.screenshot()
#             img.save(f'{name}.png')
#             print("Screen shot has been saved in the main folder Sir.. You may check.")
#             speak("Screen shot has been saved in the main folder Sir.. You may check.")

#         elif 'where i am' in query or 'where we are' in query or "location" in query:
#             speak('Searching Location Sir')
#             ip = get("https://api.ipify.org").text
#             print(f"Your IP Address is {ip} Sir.... ")
#             try:
#                 url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
#                 geo = get(url)
#                 data = geo.json()

#                 city = data['city']
#                 country = data['country']
#                 print(f"I am not sure Sir but I think that we are in {city},{country}")
#                 speak(f"I am not sure Sir but I think that we are in {city},{country}")
#             except:
#                 speak("Due to network issue I can't find the location")
        
#         elif 'check profile'in query or "check insta profile" in query:
#             speak("Write the name of the profile Sir")
#             id = input("Write the profile name: ")
#             speak(f"Opening profile Sir")
#             webbrowser.open(f"www.instagram.com/{id}")
#             time.sleep(6)
#             speak("Do you want to download the profile picture Sir")
#             condition = takecommand()
#             if 'yes' in condition:
#                 img = instaloader.Instaloader()
        
#                 img.download_profile(id,profile_pic_only=True)
#                 speak("Downloading Picture Sir!")
#                 time.sleep(3)
#                 speak("Picture has been downloaded in the main folder")
#         elif "where is" in query:
#             query = query.replace("where is","")
#             location=query
#             speak(f"Locating {location} Sir!....")
#             time.sleep(2)
#             webbrowser.open(f"https://google.co.in/maps/place/{location}")
#         elif "wikipedia" in query:
#             speak("Searching Wikipedia ")
#             query = query.replace("wikipedia","")
#             result = wikipedia.summary(query,sentences=2)
#             print(result)
#             speak("According to wikipedia" + result)
#         elif "hide" in query or "visible" in query:
#             speak("Do you want to hide the files or make the files visible?")
#             chk = takecommand()
#             if 'hide' in chk:
#                 os.system('attrib +h /s /d')
#                 speak("Sir ,All the files in the folder are hidden now")
#             elif 'visible' in chk:
#                 os.system('attrib -h /s /d')
#                 speak("Sir ,All the files in the folder are visible now")
#             elif 'leave' in chk:
#                 speak("Ok Sir!..")
#         elif 'sleep' in query or 'exit' in query:
#             print("Thanks for using me Sir....See you soon")
#             speak("Thanks for using me Sir....See you soon")
#             sys.exit()
#         elif 'battery' in query :
#             battery = psutil.sensors_battery()
#             percentage = battery.percent
#             type(percentage)
#             print(f'Sir our system has {percentage} percent battery')
#             speak(f'Sir our system has {percentage} percent battery')
#             if percentage >75:
#                 print("We have lot of power to do work")
#                 speak("We have lot of power to do work")
#             elif percentage >50 or percentage <=75:
#                 print("We have enough power to do work")
#                 speak("We have enough power to do work")
#             elif percentage > 20 or percentage <=50:
#                 print("We have low power Sir")
#                 speak("We have low power Sir")
#             else:
#                 print("Power too low sir you should charge")
#                 speak("Power too low sir you should charge")

#         elif 'internet speed' in query or 'speed' in query:
#             speak('Checking Internet Speed Sir')
        
        
#             download_speed, upload_speed = check_internet_speed()

            
#             print(f"Download speed: {results['download'] / 1000000:.2f} Mbps")
#             speak(f"Download speed: {results['download'] / 1000000:.2f} Mbps")
            
            
#             print(f"Upload speed: {results['upload'] / 1000000:.2f} Mbps")
#             speak(f"Upload speed: {results['upload'] / 1000000:.2f} Mbps")
            
#         elif 'recycle' in query:
#             if is_recycle_bin_empty():
#                 print("The Recycle Bin is already empty.")
#                 speak("The Recycle Bin is already empty.")
#             else:
#                 speak('In progess Sir')
#                 winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
#                 print("Sir, Recycle bin has successfully emptied")
#                 speak("Sir, Recycle bin has successfully emptied")
#         elif 'volume up' in query:
#             pg.press('volume up')
#             speak('Done Sir')
            
#         elif 'volume down' in query:
#             pg.press('volume down')
#             speak('Done Sir')

#         elif 'volume mute' in query or 'mute' in query:
#             pg.press('volume mute')
#             speak('Done Sir')
        
#         elif 'volume full' in query:
#             for x in range(50):
#                 pg.press('volumeup')
#                 sleep(0.1) 
#             speak('Done Sir')

#         else:
#             res = chatBot(query)
#             eel.DisplayMessage(res)()  

#     except:
#         eel.DisplayMessage('Say it again Sir')
    
#     eel.ShowHood()()

