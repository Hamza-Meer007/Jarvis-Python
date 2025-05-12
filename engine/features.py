import os
import re
import webbrowser
import pygame.mixer as sound
import eel
import pywhatkit as kit
import sqlite3
from .helper import extract_yt_term, speak
from .config import ASSISTANT_NAME
sound.init()

conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()

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
                speak(f"{query} is not running or not found")
                print(f"{query} is not running or not found")

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
