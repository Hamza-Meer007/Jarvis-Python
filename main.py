import eel
import os
from jarvis import *
from engine.command import *
from engine.features import playassistantsound
def start():
   
    eel.init('www')
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    playassistantsound()
    eel.start('index.html',mode= None,host ='localhost',block=True)

