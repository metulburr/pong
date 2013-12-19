

import pygame as pg

class MenuState:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.options = ['Play', 'Quit']
        self.text_color = (255,255,255)
        self.update_text()
        self.done = False
        self.bg_color = (25,25,25)
        self.next = "GAME"
        
    def update_text(self):
        self.text,self.text_rect = self.make_text("Start Game",
            self.text_color, (self.screen_rect.centerx,100), 50)
        
    def is_hover(self):
        if self.text_rect.collidepoint(pg.mouse.get_pos()):
            return True
        else:
            return False
            
    def adjust_text_color(self):
        if self.is_hover():
            self.text_color = (255,0,0)
        else:
            self.text_color = (255,255,255)
        self.update_text()
    
    def get_event(self, event, keys):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.text_rect.collidepoint(pg.mouse.get_pos()):
                self.done = True
                self.next = 'GAME'

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        pg.display.set_caption("Pong")
        self.adjust_text_color()
            

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.text,self.text_rect)
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
