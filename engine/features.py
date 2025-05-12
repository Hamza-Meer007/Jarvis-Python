
import os
import re
import pygame.mixer as sound
import eel
import pywhatkit as kit

from helper import speak
from config import ASSISTANT_NAME
sound.init()

@eel.expose
def playassistantsound():
    

    music1= 'www\\Assets\\start_sound.mp3'
    sound.music.load(music1)
    sound.music.play()
    
    
def openCommands(query):
    query = query.replace(ASSISTANT_NAME,'')
    query = query.replace("open",'')
    query.lower()
    
    if query !="":
        speak(f"Opening {query}")
        print(f"Opening {query}")
        os.system(f"start {query}")
    else:
        speak("Not found")
  
def closeCommands(query):
    query = query.replace(ASSISTANT_NAME,'')
    query = query.replace("close",'')
    query.lower()
    query = query.strip()
        
    if not query.endswith(".exe"):
        query += ".exe"  # Ensure the process name includes the .exe extension
    
    result = os.system(f"tasklist | findstr /i {query}")
    if result == 0:  # Process found
        os.system(f"taskkill /f /im {query}")
        speak(f"Closed {query.split('.')[0]}")
        print(f"Closed {query}")
    else:
        speak(f"{query} is not running or not found")
        print(f"{query} is not running or not found")
        
        
def playYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Playing {search_term} on youtube")
        kit.playonyt(search_term)
    else:
        speak("Please specify a search term for YouTube.")
        print("Please specify a search term for YouTube.")
    
def extract_yt_term(command):
    # Updated regex to handle more variations
    pattern = r'play\s+(.*?)\s+(on\s+youtube|on\s+YouTube|on\s+yt)'
    match = re.search(pattern, command, re.IGNORECASE)
    
    return match.group(1) if match else None