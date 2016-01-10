

import pygame as pg
from .. import tools
from ..GUI import button

class KeyBinding(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('Key Bindings', (75,75,75), (self.screen_rect.centerx, 75), 75)
        self.pre_render_options()
        self.from_bottom = 400
        self.spacer = 75
        self.set_buttons()
        
        self.key_up_text, self.key_up_text_rect = self.make_text('UP', (75,75,75), (self.screen_rect.centerx - 90, 140), 20)
        self.key_down_text, self.key_down_text_rect = self.make_text('DOWN', (75,75,75), (self.screen_rect.centerx - 90, 175), 20)

        
    def set_buttons(self):
        self.up_button_settings = {
            'text' : '{}'.format(pg.key.name(self.controller_dict['up'])),
            'hover' : (255,255,255),
            'font' : None,
            'fg' : (0,0,0),
            'bg' : (155,155,155),
            'border' : False,
            'fontsize': 15,
            'command' : self.up_bind
        }
        self.down_button_settings = {
            'text' : '{}'.format(pg.key.name(self.controller_dict['down'])),
            'hover' : (255,255,255),
            'font' : None,
            'fg' : (0,0,0),
            'bg' : (155,155,155),
            'border' : False,
            'fontsize': 15,
            'command' : self.down_bind
        }
        
        btn_width = 100
        btn_height = 25
        centerX = self.screen_rect.centerx - btn_width / 2
        centerY = self.screen_rect.centery - btn_width / 2
        self.up_keybinding = button.Button((centerX,125,btn_width,btn_height), **self.up_button_settings)
        self.down_keybinding = button.Button((centerX,160,btn_width,btn_height), **self.down_button_settings)
        self.buttons = [self.up_keybinding, self.down_keybinding]

    def up_bind(self):
        self.action = 'up'
        self.next = 'GETKEY'
        self.done = True
        
    def down_bind(self):
        self.set_buttons()
        self.action = 'down'
        self.next = 'GETKEY'
        self.done = True
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key in [pg.K_UP, pg.K_w]:
                self.change_selected_option(-1)
            elif event.key in [pg.K_DOWN, pg.K_s]:
                self.change_selected_option(1)
            elif event.key == pg.K_RETURN:
                self.select_option(self.selected_index)
                
            elif event.key == self.controller_dict['back']:
                #self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'
        self.mouse_menu_click(event)
        for button in self.buttons:
            button.get_event(event)

    def update(self, now, keys):
        #pg.mouse.set_visible(True)
        self.mouse_hover_sound()
        self.change_selected_option()
        for button in self.buttons:
            button.update()

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.key_up_text,self.key_up_text_rect)
        screen.blit(self.key_down_text,self.key_down_text_rect)
        for button in self.buttons:
            button.render(screen)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        
    def cleanup(self):
        pass

    def entry(self):
        pass
