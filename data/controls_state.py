
import pygame as pg
from .sound import Sound

class Controls:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.listings = [
            'W = Left Paddle move up', 
            'S = Left Paddle move down',
            'Up Arrow = Right Paddle move up',
            'Down Arrow = Right Paddle move down',
            'Esc = go to main menu']
        self.title, self.title_rect = self.make_text('Controls', (75,75,75), (self.screen_rect.centerx, 75), 70)
        self.text_basic_color = (255,255,255)
        self.text_hover_color = (255,0,0)
        self.text_color = self.text_basic_color 
        self.done = False
        self.bg_color = (25,25,25)
        self.next = "PLAY"
        self.timer = 0.0
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 25
        self.quit = False
        self.sound_init()
        
    def sound_init(self):
        self.button_sound = Sound('resources/sound/button.wav')
        self.button_sound.sound.set_volume(.1)
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        pg.display.set_caption("Pong")
        if self.quit:
            return True

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            screen.blit(opt[0],opt[1])
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def pre_render_options(self):
        listing_text = pg.font.Font("resources/fonts/Megadeth.ttf",25)
        #font_selected = pg.font.Font("resources/fonts/Megadeth.ttf",75)

        rendered_msg = {"des":[],"sel":[]}
        for listing in self.listings:
            text = listing_text.render(listing, 1, (255,255,255))
            text_rect = text.get_rect()
            rendered_msg["des"].append((text, text_rect))
        self.rendered = rendered_msg
