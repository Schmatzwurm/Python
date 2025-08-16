import pygame

from ..base import utils

class Tank:
    def __init__(self, screen):
        image_file_path = utils.get_res_file_path('tank.png')
        image = pygame.image.load(image_file_path)
        self._image_right = pygame.transform.scale(image, (180, 150))
        self._image_left = pygame.transform.flip(self.image_right, True, False)
        self._image = self.image_right
        self._screen = screen
        

    def draw(self, x, y):
        self._screen.blit(self._image, (x, y))


    