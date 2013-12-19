
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
            self.state.get_event(event, self.keys)
        self.state.const_event(self.keys)

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


