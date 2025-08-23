from ..base import utils
from ..base import options

import pygame


class BaseMenu:
    def __init__(self, screen, options=options.Options()):
        image_file_path = utils.get_res_file_path('menu_bg.jpg')
        image = pygame.image.load(image_file_path)
        self._screen = screen
        self._options = options
        self._background_image = pygame.transform.scale(image, screen.get_size())
        self._screen.blit(self._background_image, (0, 0))

