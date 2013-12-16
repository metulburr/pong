
import pygame as pg

class Ball:
    def __init__(self, screen_rect, width, height, color=(255,255,255)):
        self.width = width
        self.height = height
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.rect.center = screen_rect.center
        self.color = color
        self.surface.fill(self.color)
        self.speed = 20
        
    def move(self, x, y):
        self.rect[0] += x * self.speed
        self.rect[1] += y * self.speed
        
    def update(self):
        pass
        
    def render(self, screen):
        screen.blit(self.surface, self.rect)
        
