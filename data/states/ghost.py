
from . import classic
from .. import ball as ball_
import random
import pygame as pg

class Ghost(classic.Classic):
    def __init__(self, screen_rect):
        classic.Classic.__init__(self, screen_rect)
        self.fake_balls = []
        
    def add_fake_ball(self):
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball = ball_.Ball(self.screen_rect, 10,10, color, menu=True)
        self.fake_balls.append(ball)
        
    def adjust_score(self, hit_side):
        if hit_side == -1:
            self.add_fake_ball()
            self.score[1] += 1
        elif hit_side == 1:
            self.add_fake_ball()
            self.score[0] += 1
            
    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.score_text, self.score_rect)
        self.ball.render(screen)
        for ball in self.fake_balls:
            ball.render(screen)
        self.paddle_left.render(screen)
        self.paddle_right.render(screen)
        if self.pause:
            screen.blit(self.pause_text, self.pause_rect)
            
    def update(self, now, keys):
        self.ai.update(self.ball.rect, self.ball, self.paddle_left.rect)
        if not self.pause:
            self.score_text, self.score_rect = self.make_text('{}:{}'.format(self.score[0], self.score[1]),
                (255,255,255), (self.screen_rect.centerx,25), 50)
            self.paddle_left.update(self.screen_rect)
            self.paddle_right.update(self.screen_rect)
            hit_side = self.ball.update(self.paddle_left.rect, self.paddle_right.rect)
            for ball in self.fake_balls:
                ball.update(self.bogus_rect, self.bogus_rect)
            if hit_side:
                self.adjust_score(hit_side)
        else:
            self.pause_text, self.pause_rect = self.make_text("PAUSED",
                (255,255,255), self.screen_rect.center, 50)
        pg.mouse.set_visible(False)
        self.movement(keys)
        if self.quit:
            return True
        self.ai.reset()
        
    def cleanup(self):
        pg.mixer.music.stop()
        self.background_music.setup(self.background_music_volume)
        self.fake_balls = []
        
