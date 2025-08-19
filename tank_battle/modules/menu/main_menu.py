
import game
import pygame
import sys

from ..base import utils
from ..base import button

from . import options_menu

pygame.init()
pygame.mixer.init()

class Menu:
    def __init__(self, screen):
        image_file_path = utils.get_res_file_path('menu_bg.jpg')
        image = pygame.image.load(image_file_path)
        self._background_image = pygame.transform.scale(image, screen.get_size())
        self._screen = screen
        self._options = options_menu.Menu(screen)

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(utils.get_res_file_path('font.ttf'), size)
    
    def get_options(self):
        return self._options

    def run(self):
            # Musik nur starten, wenn sie nicht läuft
        if self._options.get_music_on():
            pygame.mixer.music.load(utils.get_res_file_path('retro.mp3'))
            pygame.mixer.music.play(-1)

        while True:
           
            titel = utils.texts[utils.language]["menu_title"]
            play_text = utils.texts[utils.language]["play"]
            options_text = utils.texts[utils.language]["options"]
            quit_text = utils.texts[utils.language]["quit"]
            
            
            self._screen.blit(self._background_image, (0, 0))

            mouse_pos = pygame.mouse.get_pos()

            text = Menu.get_font(65).render(titel, True, "#b68f40")
            rect = text.get_rect(center=(640, 100))

          
            def scale_button_image(image_path, text, font):
                image = pygame.image.load(image_path)
                text_surface = font.render(text, True, "#000000")
                w = max(image.get_width(), text_surface.get_width() + 40)
                h = image.get_height()
                return pygame.transform.scale(image, (w, h))

            play_button = button.Button(
                image=scale_button_image(utils.get_res_file_path('play_rect.png'), play_text, Menu.get_font(75)),
                pos=(640, 250),
                text_input=play_text, font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            options_button = button.Button(
                image=scale_button_image(utils.get_res_file_path('options_rect.png'), options_text, Menu.get_font(75)),
                pos=(640, 400),
                text_input=options_text, font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            quit_button = button.Button(
                image=scale_button_image(utils.get_res_file_path('quit_rect.png'), quit_text, Menu.get_font(75)),
                pos=(640, 550),
                text_input=quit_text, font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            

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
                        self._options.run()
                    if quit_button.check_for_input(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()