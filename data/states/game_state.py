
import pygame as pg
from ..ball import Ball
from ..paddle import Paddle
from ..sound import Sound

class GameState:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.score_text, self.score_rect = self.make_text("SCOREBOARD_PLACEHOLDER",
            (255,255,255), (screen_rect.centerx,100), 50)
        self.pause_text, self.pause_rect = self.make_text("PAUSED",
            (255,255,255), screen_rect.center, 50)
        self.done = False
        self.next = "MENU"
        self.timer = 0.0
        self.quit = False
        
        #game specific content
        self.bg_color = (0,0,0)
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
        
        self.sound_init()
        
    def sound_init(self):
        self.button_sound = Sound('button.wav')
        self.button_sound.sound.set_volume(.1)
        
    def reset(self):
        self.pause = False
        self.score = [0,0]
        self.ball.set_ball()
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'
                self.reset()
            elif event.key == pg.K_p:
                self.pause = not self.pause
                    
    def movement(self, keys):
        if keys[pg.K_w]:
            self.paddle_left.move(0, -1)
        if keys[pg.K_s]:
            self.paddle_left.move(0, 1)
        if keys[pg.K_UP]:
            self.paddle_right.move(0, -1)
        if keys[pg.K_DOWN]:
            self.paddle_right.move(0, 1)
        
    def update(self, now, keys):
        if not self.pause:
            self.score_text, self.score_rect = self.make_text('{}:{}'.format(self.score[0], self.score[1]),
                (255,255,255), (self.screen_rect.centerx,25), 50)
            self.paddle_left.update(self.screen_rect)
            self.paddle_right.update(self.screen_rect)
            hit_side = self.ball.update(self.paddle_left.rect, self.paddle_right.rect)
            if hit_side:
                self.adjust_score(hit_side)
        else:
            self.pause_text, self.pause_rect = self.make_text("PAUSED",
                (255,255,255), self.screen_rect.center, 50)
        pg.display.set_caption('Ball speed: {}'.format(self.ball.speed))
        pg.mouse.set_visible(False)
        self.movement(keys)
        if self.quit:
            return True
            

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.score_text, self.score_rect)
        self.ball.render(screen)
        self.paddle_left.render(screen)
        self.paddle_right.render(screen)
        if self.pause:
            screen.blit(self.pause_text, self.pause_rect)
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/impact.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def adjust_score(self, hit_side):
        if hit_side == -1:
            self.score[1] += 1
        elif hit_side == 1:
            self.score[0] += 1
