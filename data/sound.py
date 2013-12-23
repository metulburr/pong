
import pygame as pg
import os

class Sound:
    def __init__(self, filename):
        self.path = os.path.join('resources', 'sound')
        self.fullpath = os.path.join(self.path, filename)
        pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=128)
        self.sound = pg.mixer.Sound(self.fullpath)
        
class Music:
    def __init__(self):
        self.path = 'resources/music'
        self.load()
        
    def load(self):
        for f in os.listdir(self.path):
            end_path = os.path.join(self.path, f)
            abspath = os.path.abspath(end_path)
            pg.mixer.music.load(abspath)
            pg.mixer.music.queue(abspath)
        

