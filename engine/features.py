import os
from shlex import quote
import subprocess
import webbrowser
import pyautogui
import pygame.mixer as sound
import eel
import pywhatkit as kit
import sqlite3
from .helper import extract_yt_term, remove_words, speak
from .config import ASSISTANT_NAME
import struct
import time
import pvporcupine
import pyaudio
from hugchat.hugchat import ChatBot
sound.init()

conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()


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
            
            
            
@eel.expose
def playassistantsound():
    

    music1= 'www\\Assets\\start_sound.mp3'
    sound.music.load(music1)
    sound.music.play()
    
    
def openCommands(query):
    query = query.replace(ASSISTANT_NAME,'')
    query = query.replace("open",'')
    query.lower()
    
    app_name = query.strip()
    if app_name !=0:
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            result = cursor.fetchall()
            if len(result) !=0:
                app_path = result[0]
                os.startfile(app_path[0])
                speak(f"Opening {app_name}")
                print(f"Opening {app_name}")
            elif len(result) ==0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                result = cursor.fetchall()
                if len(result) !=0: 
                    webbrowser.open(result[0][0])
                    speak(f"Opening {app_name}")
                    print(f"Opening {app_name}")
                else:
                    speak(f"Opening {query}")
                    print(f"Opening {query}")
                    try:
                        os.system(f"start {query}")
                    except:
                        speak("Not found")
                    
        except Exception as e:
            speak("An error occurred while trying to open the application.")
            print(f"Error: {e}")
        
  
def closeCommands(query):
    query = query.replace(ASSISTANT_NAME, '')
    query = query.replace("close", '')
    query = query.lower().strip()

    try:
        # Fetch the app path from the database
        cursor.execute("SELECT path FROM sys_command WHERE LOWER(name) = LOWER(?)", (query,))
        result = cursor.fetchall()

        if result:
            app_path = result[0][0]
            print(f"App path fetched from database: {app_path}")

            # Check if the app is running
            process_name = app_path.split('\\')[-1]  # Extract the executable name
            if not process_name.endswith(".exe"):
                process_name += ".exe"

            is_running = os.system(f"tasklist | findstr /i {process_name}") == 0

            if is_running:
                os.system(f"taskkill /f /im {process_name}")
                speak(f"Closing {query}")
                print(f"Closing {query}")
            else:
                speak(f"{query} is already closed")
                print(f"{query} is already closed")
        else:
            # Attempt to close using system command with known exe paths
            if not query.endswith(".exe"):
                query += ".exe"

            print(f"Attempting to close {query} using system command...")
            is_running = os.system(f"tasklist | findstr /i {query}") == 0

            if is_running:
                os.system(f"taskkill /f /im {query}")
                speak(f"Closing {query.split('.')[0]}")
                print(f"Closing {query}")
            else:
                speak(f"{query.split('.')[0]} is not running or not found")
                print(f"{query.split('.')[0]} is not running or not found")

    except Exception as e:
        speak("An error occurred while trying to close the application.")
        print(f"Error: {e}")
        
        
def playYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Playing {search_term} on youtube")
        kit.playonyt(search_term)
    else:
        speak("Please specify a search term for YouTube.")
        print("Please specify a search term for YouTube.")



# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+92'):
            mobile_number_str = '+92' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 16
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 11
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 10
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    
    for i in range(target_tab):
        pyautogui.hotkey('tab')
        

    pyautogui.hotkey('enter')
    speak(jarvis_message)


def chatBot(query):
    user_input = query.lower()
    chatbot = ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response