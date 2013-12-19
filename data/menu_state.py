

import pygame as pg

class MenuState:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.options = ['Play', 'Quit']
        self.text,self.text_rect = self.make_text("Start Game",
            (255,255,255), (screen_rect.centerx,100), 50)
        self.done = False
        self.bg_color = (25,25,25)
        self.next = "GAME"
    
    def get_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.text_rect.collidepoint(pg.mouse.get_pos()):
                self.done = True
                self.next = 'GAME'

    def update(self, now, keys):
        pass

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.text,self.text_rect)
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
