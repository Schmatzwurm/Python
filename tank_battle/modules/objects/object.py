from ..base import utils

import pygame

class Object:
    def __init__(self, screen, size, name, pos=(0,0)):
        image_file_path = utils.get_res_file_path(name)
        image = pygame.image.load(file=image_file_path)
        self._image = pygame.transform.scale(image, size)
        self._screen = screen
        self._size = size
        self._pos = pos


    def draw(self):
        self._screen.blit(self._image, self._pos)


    def set_pos(self, pos):
        self._pos = pos


    def get_pos(self):
        return self._pos


    def get_size(self):
        return self._size
            