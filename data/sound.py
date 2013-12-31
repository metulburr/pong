
import pygame as pg
import os
import random

class Sound:
    def __init__(self, filename):
        self.path = os.path.join('resources', 'sound')
        self.fullpath = os.path.join(self.path, filename)
        pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=128)
        self.sound = pg.mixer.Sound(self.fullpath)
        
class Music:
    def __init__(self, volume):
        self.path = os.path.join('resources', 'music')
        self.setup(volume)

        
    def setup(self, volume):
        self.track_end = pg.USEREVENT+1
        self.tracks = []
        self.track = 0
        for track in os.listdir(self.path):
            self.tracks.append(os.path.join(self.path, track))
        random.shuffle(self.tracks)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.set_endevent(self.track_end)
        pg.mixer.music.load(self.tracks[0])
