import eel
import os
from engine.command import allcommands

from engine.features import playassistantsound
def start():
   
    eel.init('www')
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    playassistantsound()
    eel.start('index.html',mode= None,host ='localhost',block=True)

if __name__=="__main__":
    start()