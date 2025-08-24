from ..base import utils

import pygame

class BaseObject:
    def __init__(self, screen, image_size, image_file_path):
        image_file_path = utils.get_res_file_path(image_file_path)
        image = pygame.image.load(file=image_file_path)
        self._image = pygame.transform.scale(image, image_size)
        self._screen = screen
            