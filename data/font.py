
import pygame as pg

class Font:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
        self.surface = None
        self.font_type = "resources/fonts/Megadeth.ttf"
        self.init('0:0')
        
    def init(self, text):
        font = pg.font.Font(self.font_type, self.size)
        self.label = font.render(text, 1, self.color)
        self.label_rect = self.label.get_rect()
        #self.label_rect = self.pos

    def update(self, text, screen_rect):
        #self.label_rect.centerx = screen_rect.centerx
        self.surface = self.init(text)
        
    def render(self, screen):
        #screen.blit(self.label, self.label_rect)
        screen.blit(self.label, (screen.get_rect().centerx-(self.label_rect.width//2),0))
