from .object import Object

from ..physics.throwing_path import ThrowingPath

import pygame

class Grenade(Object):
    def __init__(self, screen, min_pos=(0,0), max_pos=(1280,720), size=(10,10), backfire=False):
        super().__init__(screen, size, 'cannon_ball.png')
        self._flying = False
        self._size = size
        self._throwing_path = ThrowingPath(min_pos=min_pos, max_pos=max_pos, invert_x=backfire, invert_y=True)


    def draw(self):
        pos = self.get_pos()
        if pos is None:
            self._flying = False
            self._throwing_path.reset()
        else:
            self._screen.blit(self._image, pos)

    
    def get_pos(self):
        if self._flying:
            return self._throwing_path.update_and_get()
        return None


    def shoot(self, start_pos, angle):
        if not self._flying:
            self._flying = True
            start_pos = (start_pos[0] - self._size[0] / 2, start_pos[1] - self._size[1] / 2)
            self._throwing_path.throw(velocity=100, time_factor=5, angle=angle, start_pos=start_pos)

