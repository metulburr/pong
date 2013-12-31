

from .sound import Sound, Music
from .ball import Ball
import pygame as pg
import random

class States:
    def __init__(self):
        self.bogus_rect = pg.Surface([0,0]).get_rect()
        self.screen_rect = self.bogus_rect
        self.button_volume = .1
        self.button_sound = Sound('button.wav')
        self.button_sound.sound.set_volume(self.button_volume)
        self.background_music_volume = .3
        self.background_music = Music(self.background_music_volume)
        self.bg_color = (25,25,25)
        self.timer = 0.0
        self.quit = False
        self.done = False
        
        self.text_basic_color = (255,255,255)
        self.text_hover_color = (255,0,0)
        self.text_color = self.text_basic_color 
        
        self.fake_ball_count = 5
    def create_fake_balls(self):
        self.fake_balls = []
        for i in range(self.fake_ball_count):
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            ball = Ball(self.screen_rect, 10,10, color, menu=True)
            self.fake_balls.append(ball)
