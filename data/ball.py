
import pygame as pg
import random
from .sound import Sound

class Ball:
    def __init__(self, screen_rect, width, height, color=(255,255,255)):
        self.width = width
        self.height = height
        self.screen_rect = screen_rect
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.center_screen = screen_rect.center
        self.color = color
        self.surface.fill(self.color)
        self.speed_init = 3
        self.speed = self.speed_init
        self.speed_incr = 0
        self.switch_speed = 5
        self.set_ball()
        self.sound_init()
        
    def sound_init(self):
        self.bounce = Sound('boing.wav')
        self.bounce.sound.set_volume(.5)
        self.gutter = Sound('whoosh.wav')
        self.gutter.sound.set_volume(.1)
        
    def get_random_float(self):
        '''get float for velocity of ball on starting direction'''
        while True:
            num = random.uniform(-1.0, 1.0)
            if num > -.5 and num < .5:
                continue
            else:
                return num
        
        
    def set_ball(self):
        #self.vel = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.vel = [self.get_random_float(), self.get_random_float()]
        self.rect.center = self.center_screen
        self.true_pos = list(self.rect.center)
        
        self.speed = self.speed_init #reset speed
        self.speed_incr = 0
        
    def collide_walls(self):
        if self.rect.x < 0:
            self.gutter.sound.play()
            self.set_ball()
            return -1
        elif self.rect.x > self.screen_rect.right:
            self.gutter.sound.play()
            self.set_ball()
            return 1
        if self.rect.y < 0 or self.rect.y > self.screen_rect.bottom - self.height:
            self.bounce.sound.play()
            self.vel[1] *= -1;
        return 0
            
    def collide_paddle(self, paddle_left_rect, paddle_right_rect):
        if self.rect.colliderect(paddle_left_rect) or self.rect.colliderect(paddle_right_rect):
            self.vel[0] *= -1;
            self.bounce.sound.play()
            self.speed_incr += 1
            
    def move(self):
        self.true_pos[0] += self.vel[0] * self.speed
        self.true_pos[1] += self.vel[1] * self.speed
        self.rect.center = self.true_pos
        
    def update(self, paddle_left_rect, paddle_right_rect):
        hit_side = self.collide_walls()
        if hit_side:
            return hit_side
        self.move()
        self.collide_paddle(paddle_left_rect, paddle_right_rect)
        if self.speed_incr >= self.switch_speed:
            self.speed += 1
            self.speed_incr = 0

    def render(self, screen):
        screen.blit(self.surface, self.rect)
        
