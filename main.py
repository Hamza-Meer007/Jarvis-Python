import eel
import os
from engine.command import allcommands
import subprocess
from engine.features import playassistantsound
from engine.helper import speak
from engine.auth import recognize
@eel.expose
def start():
   
    eel.init('www')
    playassistantsound()
    @eel.expose
    def init():
        # subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recognize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playassistantsound()
        else:
            speak("Face Authentication Fail")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html',mode= None,host ='localhost',block=True)