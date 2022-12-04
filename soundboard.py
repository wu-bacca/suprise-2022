import os
from playsound import playsound
import pygame



class SoundBoard:
    sounds: list[str]

    def __init__(self) -> None:        
        self.sounds = os.listdir('./sounds')
    
    def play_sound(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load("./sounds/alweer-een-winnaar.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
