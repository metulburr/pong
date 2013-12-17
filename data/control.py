
import os
import pygame as pg
from .ball import Ball
from .paddle import Paddle
from .font import Font

class Control:
    def __init__(self, fullscreen):
        pg.init()
        self.screensize = (800,600)
        if fullscreen:
            self.screen = pg.display.set_mode(self.screensize, pg.FULLSCREEN)
        else:
            os.environ["SDL_VIDEO_CENTERED"] = "True"
            self.screen = pg.display.set_mode(self.screensize)
        pg.display.set_caption("Pong")
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.done = False
        self.init()
        
        self.scoreboard = Font((0,0), color=(80,80,80), size=100)
        self.scoreboard.label_rect = self.screen_rect.centerx - (self.scoreboard.label_rect.width // 2)
        self.score = [0,0]
        
    def init(self):
        paddle_width = 10
        paddle_height = 100
        paddle_y = self.screen_rect.centery - (paddle_height // 2)
        padding = 25 #padding from wall
        pad_right = self.screensize[0] - paddle_width - padding
        
        self.ball = Ball(self.screen_rect, 10,10, (0,255,0))
        self.paddle_left = Paddle(padding,paddle_y, paddle_width,paddle_height, (150,150,150))
        self.paddle_right = Paddle(pad_right,paddle_y, paddle_width,paddle_height, (150,150,150))
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True
        if self.keys[pg.K_w]:
            self.paddle_left.move(0, -1)
        if self.keys[pg.K_s]:
            self.paddle_left.move(0, 1)
        if self.keys[pg.K_UP]:
            self.paddle_right.move(0, -1)
        if self.keys[pg.K_DOWN]:
            self.paddle_right.move(0, 1)
                
    def update(self):
        self.keys = pg.key.get_pressed()
        self.clock.tick(self.fps)
        self.scoreboard.update('{}:{}'.format(self.score[0], self.score[1]), self.screen_rect)
        
        self.paddle_left.update(self.screen_rect)
        self.paddle_right.update(self.screen_rect)
        hit_side = self.ball.update(self.paddle_left.rect, self.paddle_right.rect)
        if hit_side:
            self.adjust_score(hit_side)
        
    def render(self):
        self.screen.fill((0,0,0))
        self.scoreboard.render(self.screen)
        self.ball.render(self.screen)
        self.paddle_left.render(self.screen)
        self.paddle_right.render(self.screen)
        
        pg.display.update()
        
    def run(self):
        while not self.done:
            self.events()
            self.update()
            self.render()
            
            
    def adjust_score(self, hit_side):
        if hit_side == -1:
            self.score[1] += 1
        elif hit_side == 1:
            self.score[0] += 1
            
    def write(self, displaytext, color=(0,0,0), size=15, ul=False, bold=False,
            ital=False, font='timesnewroman'):
        font = pg.font.SysFont(font, size)
        font.set_underline(ul)
        font.set_bold(bold)
        font.set_italic(ital)
        label = font.render(displaytext, 1, color)
        label_rect = label.get_rect()
        return label,label_rect

