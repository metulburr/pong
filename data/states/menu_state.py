

import pygame as pg
from ..sound import Sound

class MenuState:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.options = ['Play', 'Options', 'Quit']
        self.next_list = ['MODE', 'OPTIONS']
        self.title, self.title_rect = self.make_text('Pong', (75,75,75), (self.screen_rect.centerx, 75), 150)
        self.text_basic_color = (255,255,255)
        self.text_hover_color = (255,0,0)
        self.text_color = self.text_basic_color 
        self.done = False
        self.bg_color = (25,25,25)
        #self.next = "PLAY"
        self.timer = 0.0
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75
        self.quit = False
        self.sound_init()
        
    def sound_init(self):
        self.button_sound = Sound('button.wav')
        self.button_sound.sound.set_volume(.1)
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i,opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pg.mouse.get_pos()):
                    if i == len(self.next_list):
                        self.quit = True
                    else:
                        self.button_sound.sound.play()
                        self.next = self.next_list[i]
                        self.done = True
                    break

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        pg.display.set_caption("2 Player Pong")
        if self.quit:
            return True

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if opt[1].collidepoint(pg.mouse.get_pos()):
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def pre_render_options(self):
        font_deselect = pg.font.Font("resources/fonts/Megadeth.ttf",50)
        font_selected = pg.font.Font("resources/fonts/Megadeth.ttf",75)

        rendered_msg = {"des":[],"sel":[]}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, (255,255,255))
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, (255,0,0))
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend,d_rect))
            rendered_msg["sel"].append((s_rend,s_rect))
        self.rendered = rendered_msg
