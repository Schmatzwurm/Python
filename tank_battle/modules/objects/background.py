from .base_object import BaseObject

from ..base import utils

import pygame

class Background(BaseObject):
    def __init__(self, screen):
        super().__init__(screen, (screen.get_width(), screen.get_height()), 'landscape.jpg')
        
    def draw(self):
        self._screen.blit(self._image, (0, 0)) 
