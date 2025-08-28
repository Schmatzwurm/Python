from .object import Object

from ..base import utils

import pygame

class Background(Object):
    def __init__(self, screen):
        super().__init__(screen, (screen.get_width(), screen.get_height()), 'landscape.jpg')
        
    def draw(self):
        self._screen.blit(self._image, (0, 0)) 
