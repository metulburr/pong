
import pygame as pg
from ..tools import States

class AudioState(States):
    def __init__(self, screen_rect):
        States.__init__(self)
        self.screen_rect = screen_rect
        self.listings = [
            'Background Music',
            '-/+'
        ]
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('Audio', (75,75,75), (self.screen_rect.centerx, 75), 150)
        self.text_basic_color = (255,255,255)
        self.text_hover_color = (255,0,0)
        self.text_color = self.text_basic_color 
        self.done = False
        self.bg_color = (25,25,25)
        #self.next = "PLAY"
        self.timer = 0.0
        self.pre_render_options()
        self.pre_render_listings()
        self.from_bottom = 400
        self.from_bottom_listings = 225
        self.spacer = 25
        self.quit = False
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
            if event.key == pg.K_ESCAPE:
                self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'
            elif event.key in [pg.K_PLUS, pg.K_EQUALS]:
                self.bg_music_modify(.1, 'play')
            elif event.key in [pg.K_MINUS, pg.K_UNDERSCORE]:
                self.bg_music_modify(-.1, 'play')
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i,opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pg.mouse.get_pos()):
                    if i == len(self.next_list):
                        self.quit = True
                    else:
                        self.button_sound.sound.play()
                        self.next = self.next_list[i]
                        #self.menu_selections.append(self.next_list[i])
                        self.done = True
                    break

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        if self.quit:
            return True

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.bg_music_num, self.bg_music_num_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if opt[1].collidepoint(pg.mouse.get_pos()):
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        for i,opt in enumerate(self.rendered_listing['des']):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom_listings + i * self.spacer)
            screen.blit(opt[0],opt[1])
                
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def pre_render_listings(self):
        listing_text = pg.font.Font("resources/fonts/impact.ttf",25)
        rendered_msg = {"des":[],"sel":[]}
        for listing in self.listings:
            text = listing_text.render(listing, 1, (255,255,255))
            text_rect = text.get_rect()
            rendered_msg["des"].append((text, text_rect))
        self.rendered_listing = rendered_msg
        
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

    def cleanup(self):
        pass
        
    def entry(self):
        pass
