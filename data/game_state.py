
from .ball import Ball
from .paddle import Paddle
from .font import Font
import pygame as pg

class Game:
    def __init__(self, screen_rect, screensize):
        self.screen_rect = screen_rect
        self.pause = False
        self.score = [0,0]
                
        paddle_width = 10
        paddle_height = 100
        paddle_y = self.screen_rect.centery - (paddle_height // 2)
        padding = 25 #padding from wall
        pad_right = screensize[0] - paddle_width - padding
        
        self.ball = Ball(self.screen_rect, 10,10, (0,255,0))
        self.paddle_left = Paddle(padding,paddle_y, paddle_width,paddle_height, (150,150,150))
        self.paddle_right = Paddle(pad_right,paddle_y, paddle_width,paddle_height, (150,150,150))
        self.scoreboard = Font((self.screen_rect.centerx , 50), color=(80,80,80), size=100)
        self.pause_notice = Font(self.screen_rect.center, color=(255,255,255), size=60)
        
    def run(self):
        if not self.pause:
            self.scoreboard.update('{}:{}'.format(self.score[0], self.score[1]), self.screen_rect)
            self.paddle_left.update(self.screen_rect)
            self.paddle_right.update(self.screen_rect)
            hit_side = self.ball.update(self.paddle_left.rect, self.paddle_right.rect)
            if hit_side:
                self.adjust_score(hit_side)
        else:
            self.pause_notice.update('PAUSED', self.screen_rect)
        pg.display.set_caption('Ball speed: {}'.format(self.ball.speed))

    def adjust_score(self, hit_side):
        if hit_side == -1:
            self.score[1] += 1
        elif hit_side == 1:
            self.score[0] += 1
        
    def render(self, screen):
            self.scoreboard.render(screen)
            self.ball.render(screen)
            self.paddle_left.render(screen)
            self.paddle_right.render(screen)
            if self.pause:
                self.pause_notice.render(screen)
