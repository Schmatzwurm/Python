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
        
    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._screen.fill("white")

            text = Menu.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            rect = text.get_rect(center=(640, 260))
            self._screen.blit(text, rect)

            back = button.Button(image=None, pos=(640, 460), 
                                 text_input="BACK", font=Menu.get_font(75), base_color="Black", hovering_color="Green")

            back.change_color(mouse_pos)
            back.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back.check_for_input(mouse_pos):
                        return         

            pygame.display.update()
