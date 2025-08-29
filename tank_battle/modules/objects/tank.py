from .object import Object
from .grenade import Grenade

from ..base import utils

import pygame
import numpy

class Tank(Object):
    def __init__(self, screen, size=(60, 50), 
                 init_pos=(0,0), min_pos=(0,0), max_pos=(1280,720), 
                 reverse=False):
        super().__init__(screen, size, name='tank.png', pos=init_pos, min_pos=min_pos, max_pos=max_pos)
        if reverse:
            self._image = pygame.transform.flip(self._image, True, False)
        self._reverse = reverse
        self._size = size
        self._pipe_out_pos = [0, 0]
        self._pipe_angle = 0
        self._pipe_length = 25
        self._grenade = Grenade(screen, min_pos=(0,0), max_pos=(1280,520), backfire=reverse)


    def draw(self):
        self._grenade.draw()

        self._screen.blit(self._image, self._pos)
        start_pos, end_pos = self.get_pipe_coord()

        pygame.draw.line(self._screen, (0,0,0), start_pos, end_pos, 5)


    def collides_with(self, obj):
        tank_rect = pygame.Rect(self._pos[0], self._pos[1], self._size[0], self._size[1])
        obj_pos = obj.get_pos()
        obj_size = obj.get_size()
        if obj_pos is None or obj_size is None:
            return False
        obj_rect = pygame.Rect(obj_pos[0], obj_pos[1], obj_size[0], obj_size[1])
        return tank_rect.colliderect(obj_rect)


    def pipe_angle(self, delta_angle):
        new_angle = self._pipe_angle + delta_angle
        if new_angle < 0:
            new_angle = 0
        elif new_angle > 90:
            new_angle = 90
        self._pipe_angle = new_angle


    def get_pipe_coord(self):
        start_pos = [0, 0]
        start_pos[1] = self._pos[1] + 13
        if self._reverse:
            start_pos[0] = self._pos[0] + 32
            actual_angle = 180 + self._pipe_angle
        else:
            start_pos[0] = self._pos[0] + 28
            actual_angle = -self._pipe_angle

        angle_rad = numpy.radians(actual_angle)    
        end_pos = (
            start_pos[0] + self._pipe_length * numpy.cos(angle_rad),
            start_pos[1] + self._pipe_length * numpy.sin(angle_rad)
        )
        return start_pos, end_pos


    def move(self, delta_x=0, delta_y=0):
        new_pos = [0, 0]
        new_pos[0] = self._pos[0] + delta_x
        new_pos[1] = self._pos[1] + delta_y

        new_pos = utils.saturate(new_pos, self._min_pos, self._max_pos)

        self._pos = new_pos


    def shoot(self):
        _, end_pos = self.get_pipe_coord()
        self._grenade.shoot(end_pos, self._pipe_angle)
        