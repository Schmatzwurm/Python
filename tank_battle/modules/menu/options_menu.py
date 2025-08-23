from . import base_menu
from . import language_menu

from ..base import options
from ..base import translations
from ..base import utils
from ..base import button

import pygame
import sys


class OptionsMenu(base_menu.Menu):
    def __init__(self, screen, options):
        super().__init__(screen, options)
    

    def apply(self):
        if not self._options.music_enabled():
            pygame.mixer.music.stop()
        else:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
        if self._options.fullscreen_toggled():
            if self._options.fullscreen_enabled():
                pygame.display.set_mode(self._screen.get_size(), pygame.FULLSCREEN)
        #else:
            #pygame.display.set_mode(self._screen.get_size())


    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._screen.fill("white")

            language = self._options.get_language()

            options_title = translations.texts[language]["options"]
            music_text = translations.texts[language]["music"]
            fullscreen_text = translations.texts[language]["fullscreen"]
            language_text = translations.texts[language]["language"]
            back_text = translations.texts[language]["back"]
            speech_value = translations.texts[language]["speech"]

            # Options
            text = utils.get_font(55).render(options_title, True, "Black")
            rect = text.get_rect(center=(640, 60))
            self._screen.blit(text, rect)

            # Music
            text = utils.get_font(40).render(music_text, True, "Black")
            rect = text.get_rect(center=(530, 250))
            self._screen.blit(text, rect)

            # Fullscreen
            text = utils.get_font(40).render(fullscreen_text, True, "Black")
            rect = text.get_rect(center=(430, 350))
            self._screen.blit(text, rect)

            # Language
            text = utils.get_font(40).render(language_text, True, "Black")
            rect = text.get_rect(center=(470, 450))
            self._screen.blit(text, rect)

            pygame.draw.line(self._screen, "Black", (200, 300), (1000, 300), 3)
            pygame.draw.line(self._screen, "Black", (200, 400), (1000, 400), 3)
            
            # Back button
            back = button.Button(image=None, pos=(150, 50), 
                                 text_input=back_text, font=utils.get_font(40), base_color="Black", hovering_color="Red")
            back.change_color(mouse_pos)
            back.update(self._screen)

            # Music button on/off
            music_enabled = self._options.music_enabled()
            music_text = "ON" if music_enabled else "OFF"
            color = "Green" if music_enabled else "Red"
            h_color = "Green" if music_enabled else "Red"
            on_or_off = button.Button(image=None, pos=(850, 250), 
                                 text_input=music_text, font=utils.get_font(40), base_color=color, hovering_color=h_color)
            on_or_off.change_color(mouse_pos)
            on_or_off.update(self._screen)

            # Fullscreen button
            fs_text = "[X]" if self._options.fullscreen_enabled() else "[ ]"
            fs_btn = button.Button(image=None, pos=(850, 350), 
                                 text_input=fs_text, font=utils.get_font(40), base_color="Black", hovering_color=False)
            fs_btn.change_color(mouse_pos)
            fs_btn.update(self._screen)

            # Language button
            lng_btn = button.Button(image=None, pos=(850, 450), 
                                 text_input=speech_value, font=utils.get_font(40), base_color="Black", hovering_color=False)
            lng_btn.change_color(mouse_pos)
            lng_btn.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back.check_for_input(mouse_pos):
                        return 
                    if on_or_off.check_for_input(mouse_pos):
                        self._options.toggle_music()
                        self.apply()

                    if fs_btn.check_for_input(mouse_pos):
                        self._options.toggle_fullscreen()
                        self.apply()

                    if lng_btn.check_for_input(mouse_pos):
                        lm = language_menu.LanguageMenu(self._screen, self._options)
                        lm.run()

            pygame.display.update()

