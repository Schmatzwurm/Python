from .options_menu import OptionsMenu
from .base_menu import BaseMenu

from ..base import utils
from ..base import button
from ..base import options
from ..base import translations

import pygame
import sys

pygame.init()
pygame.mixer.init()

class MainMenu(BaseMenu):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self._options_menu = OptionsMenu(screen, options)


    def run(self):
        # Only start music if music option is on
        if self._options.music_enabled():
            pygame.mixer.music.load(utils.get_res_file_path('retro.mp3'))
            pygame.mixer.music.play(-1)

        while True:
            language = self._options.get_language()
            title_text = translations.texts[language]["menu_title"]
            play_text = translations.texts[language]["play"]
            options_text = translations.texts[language]["options"]
            quit_text = translations.texts[language]["quit"]
            
            self._screen.blit(self._background_image, (0, 0))

            mouse_pos = pygame.mouse.get_pos()

            text = utils.get_font(65).render(title_text, True, "#b68f40")
            rect = text.get_rect(center=(640, 100))

            def scale_button_image(image_path, text, font):
                image = pygame.image.load(image_path)
                text_surface = font.render(text, True, "#000000")
                w = max(image.get_width(), text_surface.get_width() + 40)
                h = image.get_height()
                return pygame.transform.scale(image, (w, h))

            play_button = button.Button(
                image=scale_button_image(utils.get_res_file_path('play_rect.png'), play_text, utils.get_font(75)),
                pos=(640, 250),
                text_input=play_text, font=utils.get_font(75), base_color="#d7fcd4", hovering_color="White")
            options_button = button.Button(
                image=scale_button_image(utils.get_res_file_path('options_rect.png'), options_text, utils.get_font(75)),
                pos=(640, 400),
                text_input=options_text, font=utils.get_font(75), base_color="#d7fcd4", hovering_color="White")
            quit_button = button.Button(
                image=scale_button_image(utils.get_res_file_path('quit_rect.png'), quit_text, utils.get_font(75)),
                pos=(640, 550),
                text_input=quit_text, font=utils.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self._screen.blit(text, rect)

            for btn in [play_button, options_button, quit_button]:
                btn.change_color(mouse_pos)
                btn.update(self._screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(mouse_pos):
                        return 
                    if options_button.check_for_input(mouse_pos):
                        self._options_menu.run()
                    if quit_button.check_for_input(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
