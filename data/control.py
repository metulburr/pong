

import pygame as pg


class Control:
    def __init__(self, fullscreen):
        pg.init()
        self.screensize = (800,600)
        if fullscreen:
            self.screen = pg.display.set_mode(self.screensize, pg.FULLSCREEN)
        else:
            self.screen = pg.display.set_mode(self.screensize)
        self.screenrect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.done = False
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.done = True
                
    def update(self):
        self.keys = pg.key.get_pressed()
        self.clock.tick(self.fps)
        
    def render(self):
        pg.display.update()
        
    def run(self):
        while not self.done:
            self.events()
            self.update()
            self.render()

