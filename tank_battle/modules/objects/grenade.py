from .base_object import BaseObject

from ..physics.throwing_path import ThrowingPath

import pygame

class Grenade(BaseObject):
    def __init__(self, screen):
        super().__init__(screen, (20,20), 'cannon_ball.png')
        self._visible = True
        self._throwing_path = ThrowingPath(min_pos=(0,0), max_pos=(1280, 720))


    def draw(self):
        if self._visible:
            pos = self._throwing_path.update_and_get()
            if pos is None:
                self._visible = False
                self._throwing_path.reset()
            else:
                self._screen.blit(self._image, pos)


    def shoot(self, start_pos, angle):
        self._visible = True
        self._throwing_path.throw(velocity=100, angle=angle, start_pos=start_pos)

