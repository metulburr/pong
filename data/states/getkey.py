

import pygame as pg
from .. import tools

class GetKey(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('PLACEHOLDER', (75,75,75), (self.screen_rect.centerx, 75), 50)
        self.pre_render_options()
        self.from_bottom = 400
        self.spacer = 75
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == self.controller_dict['back']:
                #self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'
            else:
                self.update_controller_dict(self.action, event)
                self.next = 'KEYBINDING'
                self.done = True
        self.mouse_menu_click(event)

    def update(self, now, keys):
        self.title, self.title_rect = self.make_text('Change key binding for "{}"'.format(self.action), (75,75,75), (self.screen_rect.centerx, 75), 50)
        #pg.mouse.set_visible(True)
        self.mouse_hover_sound()

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        
    def make_text(self,message,color,center,size):
        font = tools.Font.load('impact.ttf', size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def cleanup(self):
        pass

    def entry(self):
        pass
