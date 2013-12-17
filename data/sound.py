
import pygame as pg


class Sound:
    def __init__(self, path):
        self.path = path
        self.sound = pg.mixer.Sound(self.path)


if __name__ == '__main__':
    pg.mixer.init()
    sound_obj = Sound('../resources/sound/boing.wav')
    sound_obj.sound.play()
    pg.time.delay(1000)
