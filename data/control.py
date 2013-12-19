
import os
import pygame as pg
from .game_state import Game
from .menu_state import Menu

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
        self.gamestate = Game(self.screen_rect, self.screensize)
        self.menustate = Menu(self.screen_rect)
        self.state = 'game'

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True
                elif event.key == pg.K_p:
                    if not self.gamestate.pause:
                        self.gamestate.pause = True
                    else:
                        self.gamestate.pause = False
        if self.keys[pg.K_w]:
            self.gamestate.paddle_left.move(0, -1)
        if self.keys[pg.K_s]:
            self.gamestate.paddle_left.move(0, 1)
        if self.keys[pg.K_UP]:
            self.gamestate.paddle_right.move(0, -1)
        if self.keys[pg.K_DOWN]:
            self.gamestate.paddle_right.move(0, 1)
                
    def update(self):
        self.keys = pg.key.get_pressed()
        self.clock.tick(self.fps)
        if self.state == 'game':
            self.gamestate.run()
        elif self.state == 'menu':
            self.menustate.run()
        
    def render(self):
        self.screen.fill((0,0,0))
        if self.state == 'game':
            self.gamestate.render(self.screen)
        elif self.state == 'menu':
            self.menustate.render(self.screen)
        pg.display.update()
        
    def run(self):
        while not self.done:
            self.events()
            self.update()
            self.render()
            



