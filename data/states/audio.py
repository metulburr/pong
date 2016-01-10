
import pygame as pg
from .. import tools

class Audio(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.listings = [
            'Background Music',
            '-/+'
        ]
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('Audio', (75,75,75), (self.screen_rect.centerx, 75), 150)
        self.pre_render_options()
        self.pre_render_listings()
        self.from_bottom = 400
        self.from_bottom_listings = 225
        self.spacer = 25
        self.bg_music_modify(0)
        
    def bg_music_modify(self, amount, sound=None):
            
        self.background_music_volume += amount
        if self.background_music_volume > .9:
            self.background_music_volume = 1.0
            volume_display = 'Max'
        elif self.background_music_volume < .1:
            self.background_music_volume = 0.0
            volume_display = 'Mute'
        else:
            if sound:
                self.button_sound.sound.play()
            volume_display = '{:.1f}'.format(self.background_music_volume)
        self.bg_music_num, self.bg_music_num_rect = self.make_text(
            volume_display, (75,75,75), (self.screen_rect.centerx + 125, 250), 30)
        self.background_music.setup(self.background_music_volume)
    
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
            elif event.key in [pg.K_PLUS, pg.K_EQUALS]:
                self.bg_music_modify(.1, 'play')
            elif event.key in [pg.K_MINUS, pg.K_UNDERSCORE]:
                self.bg_music_modify(-.1, 'play')
        self.mouse_menu_click(event)

    def update(self, now, keys):
        #pg.mouse.set_visible(True)
        self.mouse_hover_sound()
        self.change_selected_option()

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.bg_music_num, self.bg_music_num_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        for i,opt in enumerate(self.rendered_listing['des']):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom_listings + i * self.spacer)
            screen.blit(opt[0],opt[1])
        
    def pre_render_listings(self):
        listing_text = tools.Font.load('impact.ttf', 25)
        rendered_msg = {"des":[],"sel":[]}
        for listing in self.listings:
            text = listing_text.render(listing, 1, (255,255,255))
            text_rect = text.get_rect()
            rendered_msg["des"].append((text, text_rect))
        self.rendered_listing = rendered_msg

    def cleanup(self):
        pass
        
    def entry(self):
        pass
