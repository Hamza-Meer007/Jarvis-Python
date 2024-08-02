import eel
import os
from jarvis import *
from command import *

def start():
    # eel.init('www')
    # # os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # play()
    # eel.start('index.html',mode= 'default',host ='localhost',block=True)
    eel.init('www')
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    play()
    eel.start('index.html',mode= None,host ='localhost',block=True)

