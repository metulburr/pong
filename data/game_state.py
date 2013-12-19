
from .ball import Ball
from .paddle import Paddle
from .font import Font
import pygame as pg


import pygame as pg

class GameState:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.options = ['Play', 'Quit']
        self.text,self.text_rect = self.make_text("GAME",
            (255,255,255), (screen_rect.centerx,100), 50)
        self.done = False
        self.bg_color = (0,0,0)
        self.next = "MENU"
        
        #game specific content
        self.keys = pg.key.get_pressed()
        self.pause = False
        self.score = [0,0]
                
        paddle_width = 10
        paddle_height = 100
        paddle_y = self.screen_rect.centery - (paddle_height // 2)
        padding = 25 #padding from wall
        pad_right = screen_rect.width - paddle_width - padding
        
        self.ball = Ball(self.screen_rect, 10,10, (0,255,0))
        self.paddle_left = Paddle(padding,paddle_y, paddle_width,paddle_height, (150,150,150))
        self.paddle_right = Paddle(pad_right,paddle_y, paddle_width,paddle_height, (150,150,150))
        self.scoreboard = Font((self.screen_rect.centerx , 50), color=(80,80,80), size=100)
        self.pause_notice = Font(self.screen_rect.center, color=(255,255,255), size=60)
        
    def reset(self):
        self.pause = False
        self.score = [0,0]
        self.ball.set_ball()
        
    
    def get_event(self,event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
                self.next = 'MENU'
                self.reset()
            elif event.key == pg.K_p:
                if not self.pause:
                    self.pause = True
                else:
                    self.pause = False
        #elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        #    if self.text_rect.collidepoint(pg.mouse.get_pos()):
        #        self.done = True
        if self.keys[pg.K_w]:
            self.paddle_left.move(0, -1)
        if self.keys[pg.K_s]:
            self.paddle_left.move(0, 1)
        if self.keys[pg.K_UP]:
            self.paddle_right.move(0, -1)
        if self.keys[pg.K_DOWN]:
            self.paddle_right.move(0, 1)


    def update(self, now, keys):
        self.keys = pg.key.get_pressed()
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

    def render(self, screen):
        screen.fill(self.bg_color)
        #screen.blit(self.text,self.text_rect)
        
        self.scoreboard.render(screen)
        self.ball.render(screen)
        self.paddle_left.render(screen)
        self.paddle_right.render(screen)
        if self.pause:
            self.pause_notice.render(screen)
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def adjust_score(self, hit_side):
        if hit_side == -1:
            self.score[1] += 1
        elif hit_side == 1:
            self.score[0] += 1
