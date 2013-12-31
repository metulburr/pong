

from .sound import Sound, Music

class States:
    def __init__(self):
        self.menu_selections = []
        self.button_volume = .1
        self.button_sound = Sound('button.wav')
        self.button_sound.sound.set_volume(self.button_volume)
        self.background_music_volume = .3
        self.background_music = Music(self.background_music_volume)
    
