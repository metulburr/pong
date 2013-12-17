
import pygame as pg
import random

class Ball:
    def __init__(self, screen_rect, width, height, color=(255,255,255)):
        self.screen_rect = screen_rect
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.rect.center = screen_rect.center
        self.color = color
        self.surface.fill(self.color)
        self.speed = 5
        self.vel = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.true_pos = list(self.rect.center)
        
    def collide_walls(self):
        if self.rect.x < 0 or self.rect.x > self.screen_rect.right:
            self.vel[0] *= -1;
        elif self.rect.y < 0 or self.rect.y > self.screen_rect.bottom:
            self.vel[1] *= -1;
            
    def collide_paddle(self, paddle_left_rect, paddle_right_rect):
        if self.rect.colliderect(paddle_left_rect) or self.rect.colliderect(paddle_right_rect):
            self.vel[0] *= -1;
            
    def move(self):
        self.true_pos[0] += self.vel[0] * self.speed
        self.true_pos[1] += self.vel[1] * self.speed
        self.rect.center = self.true_pos
        
    def update(self, paddle_left_rect, paddle_right_rect):
        self.collide_walls()
        self.move()
        self.collide_paddle(paddle_left_rect, paddle_right_rect)

    def render(self, screen):
        screen.blit(self.surface, self.rect)
        
