from ..base import utils

import pygame

class BaseObject:
    def __init__(self, screen, image_file_path=None):
        self._screen = screen
        self._image = None
        if image_file_path:
            image_file_path = utils.get_res_file_path(image_file_path)
            image = pygame.image.load(file=image_file_path)
            self._image = pygame.transform.scale(image, 
                (screen.get_width(), screen.get_height()))
            