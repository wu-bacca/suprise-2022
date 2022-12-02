import os
import random
from playsound import playsound


class SoundBoard:
    sounds: list[str]

    def __init__(self) -> None:        
        self.sounds = os.listdir('./sounds')
    
    def play_random_sound(self) -> None:        
        sound_to_play = f'./sounds/{random.choice(self.sounds)}'
        playsound(sound = sound_to_play)
