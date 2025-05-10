
import pygame.mixer as sound
import eel
sound.init()

@eel.expose
def playassistantsound():

    music1= 'www\\Assets\\start_sound.mp3'
    sound.music.load(music1)
    sound.music.play()