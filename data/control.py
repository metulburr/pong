
import os
import pygame as pg
from .game_state import GameState
from .menu_state import MenuState

class Control:
    def __init__(self, fullscreen):
        pg.init()
        self.screensize = (800,600)
        if fullscreen:
            self.screen = pg.display.set_mode(self.screensize, pg.FULLSCREEN)
        else:
            os.environ["SDL_VIDEO_CENTERED"] = "True"
            self.screen = pg.display.set_mode(self.screensize)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.done = False
        self.state_dict = {
            "MENU" : MenuState(self.screen_rect),
            "GAME"  : GameState(self.screen_rect)
        }
        self.state_name = "MENU"
        self.state = self.state_dict[self.state_name]

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN,pg.KEYUP):
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)

    def change_state(self):
        if self.state.done:
            self.state_name = self.state.next
            self.state.done = False
            self.state = self.state_dict[self.state_name]

    def run(self):
        while not self.done:
            now = pg.time.get_ticks()
            self.event_loop()
            self.change_state()
            self.state.update(now, self.keys)
            self.state.render(self.screen)
            pg.display.update()
            self.clock.tick(self.fps)

class Control2:
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
        #self.gamestate = Game(self.screen_rect, self.screensize)
        #self.menustate = Menu(self.screen_rect)
        #self.state = 'game'
        
        
        self.state_dict = {
            "MENU" : MenuState(self.screen_rect),
            "GAME"  : GameState(self.screen_rect, self.screensize)
        }
        self.state_name = "MENU"
        self.state = self.state_dict[self.state_name]

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
        self.state.get_event(event)
                
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
            



