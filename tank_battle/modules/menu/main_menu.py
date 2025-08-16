from ..base import utils
import game
import pygame
import sys
from ..base import button

pygame.init()
pygame.mixer.init()

class Menu:
    def __init__(self, screen):
        image_file_path = utils.get_res_file_path('menu_bg.jpg')
        image = pygame.image.load(image_file_path)
        self._background_image = pygame.transform.scale(image, screen.get_size())
        self._screen = screen

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(utils.get_res_file_path('font.ttf'), size)

    def play():
        game.main()
        
    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self._screen.fill("white")

            OPTIONS_TEXT = Menu.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self._screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = button.Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=Menu.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.change_color(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
                        return
                        

            pygame.display.update()

    def run(self):
            # Musik nur starten, wenn sie nicht läuft
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(utils.get_res_file_path('retro.mp3'))
            pygame.mixer.music.play(-1)

        while True:
           


            self._screen.blit(self._background_image, (0, 0))

            mouse_pos = pygame.mouse.get_pos()

            MENU_TEXT = Menu.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = button.Button(
                image=pygame.image.load(utils.get_res_file_path('play_rect.png')), 
                pos=(640, 250), 
                text_input="PLAY", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = button.Button(
                image=pygame.image.load(utils.get_res_file_path('options_rect.png')), 
                pos=(640, 400), 
                text_input="OPTIONS", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = button.Button(
                image=pygame.image.load(utils.get_res_file_path('quit_rect.png')), 
                pos=(640, 550), 
                text_input="QUIT", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self._screen.blit(MENU_TEXT, MENU_RECT)

            for btn in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                btn.change_color(mouse_pos)
                btn.update(self._screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.check_for_input(mouse_pos):
                        pygame.mixer.music.stop()
                        return 
                    if OPTIONS_BUTTON.check_for_input(mouse_pos):
                        self.options()
                    if QUIT_BUTTON.check_for_input(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()