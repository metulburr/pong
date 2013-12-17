
import pygame as pg

class Font:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
        self.font_type = "resources/fonts/Megadeth.ttf"

    def update(self, text, screen_rect):
        font = pg.font.Font(self.font_type, self.size)
        self.label = font.render(text, 1, self.color)
        self.rect = self.label.get_rect(center=self.pos)
        
    def render(self, screen):
        screen.blit(self.label, self.rect)
        #screen.blit(self.label, self.pos)
