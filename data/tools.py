

from .sound import Sound, Music
import pygame as pg
import os
import shutil

def clean_files():
    '''remove all pyc files and __pycache__ direcetories in subdirectory'''
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                path = os.path.join(root, dir)
                print('removing {}'.format(os.path.abspath(path)))
                shutil.rmtree(path)
        for name in files:
            if name.endswith('.pyc'):
                path = os.path.join(root, name)
                print('removing {}'.format(os.path.abspath(path)))
                os.remove(path)


class States:
    def __init__(self):
        self.bogus_rect = pg.Surface([0,0]).get_rect()
        self.screen_rect = self.bogus_rect
        self.button_volume = .2
        self.button_hover_volume = .1
        self.button_sound = Sound('button.wav')
        self.button_sound.sound.set_volume(self.button_volume)
        self.button_hover = Sound('button_hover.wav')
        self.button_hover.sound.set_volume(self.button_hover_volume)
        self.background_music_volume = .3
        self.background_music = Music(self.background_music_volume)
        self.bg_color = (25,25,25)
        self.timer = 0.0
        self.quit = False
        self.done = False
        self.last_option = None
        
        self.text_basic_color = (255,255,255)
        self.text_hover_color = (255,0,0)
        self.text_color = self.text_basic_color 
        
    def mouse_hover_sound(self):
        for i,opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pg.mouse.get_pos()):
                if self.last_option != opt:
                    self.button_hover.sound.play()
                    self.last_option = opt
                    
    def mouse_menu_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i,opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pg.mouse.get_pos()):
                    if i == len(self.next_list):
                        self.quit = True
                    else:
                        #self.button_sound.sound.play()
                        self.next = self.next_list[i]
                        self.done = True
                    break

