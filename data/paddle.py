
import pygame as pg

class Paddle:
    def __init__(self, x, y, width, height, color=(255,255,255)):
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.surface.fill(self.color)
        self.speed = 6
        
    def move(self, x, y):
        self.rect[0] += x * self.speed
        self.rect[1] += y * self.speed
        
    def update(self, screen_rect):
        self.rect.clamp_ip(screen_rect)
        
    def render(self, screen):
        screen.blit(self.surface, self.rect)
