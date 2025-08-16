import pygame

from ..base import utils

class Background:
    def __init__(self, screen):
        image_file_path = utils.get_res_file_path('landscape.jpg')
        image = pygame.image.load(file=image_file_path)
        self._image = pygame.transform.scale(image, 
            (screen.get_width(), screen.get_heighth()))
        self._screen = screen
        
    def draw(self):
        self._screen.blit(self._image, (0, 0)) 
