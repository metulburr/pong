
import os
import pygame as pg
from .ball import Ball
from .paddle import Paddle

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
        self.ball.update()
        self.paddle_left.update(self.screen_rect)
        self.paddle_right.update(self.screen_rect)
        
    def render(self):
        self.screen.fill((0,0,0))
        self.ball.render(self.screen)
        self.paddle_left.render(self.screen)
        self.paddle_right.render(self.screen)
        pg.display.update()
        
    def run(self):
        while not self.done:
            self.events()
            self.update()
            self.render()

