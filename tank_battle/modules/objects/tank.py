from .object import Object
from .grenade import Grenade

from ..base import utils

import pygame
import numpy

class Tank(Object):
    def __init__(self, screen, size=(180, 150), 
                 init_pos=(0,0), min_pos=(0,0), max_pos=(1280,720), 
                 reverse=False):
        super().__init__(screen, size, 'tank.png')
        if reverse:
            self._image = pygame.transform.flip(self._image, True, False)
        self._reverse = reverse
        self._size = size
        self._pos_x = init_pos[0]
        self._pos_y = init_pos[1]
        self._min_pos_x = min_pos[0]
        self._min_pos_y = min_pos[1]
        self._max_pos_x = max_pos[0]
        self._max_pos_y = max_pos[1]
        self._pipe_out_pos = [0, 0]
        self._pipe_angle = 0
        self._pipe_length = 50
        self._grenade = Grenade(screen, min_pos=(0,0), max_pos=(1280,520), backfire=reverse)


    def draw(self):
        self._grenade.draw()

        self._screen.blit(self._image, (self._pos_x, self._pos_y))
        start_pos, end_pos = self.get_pipe_coord()

        pygame.draw.line(self._screen, (0,0,0), start_pos, end_pos, 5)


    def collides_with(self, obj):
        tank_rect = pygame.Rect(self._pos_x, self._pos_y, self._size[0], self._size[1])
        obj_pos = obj.get_pos()
        obj_size = obj.get_size()
        if obj_pos is None:
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
        start_pos_y = self._pos_y + 62
        if self._reverse:
            start_pos_x = self._pos_x + 72
            actual_angle = 180 + self._pipe_angle
        else:
            start_pos_x = self._pos_x + 105
            actual_angle = -self._pipe_angle

        angle_rad = numpy.radians(actual_angle)    
        end_pos = (
            start_pos_x + self._pipe_length * numpy.cos(angle_rad),
            start_pos_y + self._pipe_length * numpy.sin(angle_rad)
        )
        start_pos = (start_pos_x, start_pos_y)
        return start_pos, end_pos


    def move(self, delta_x=0, delta_y=0):
        new_pos_x = self._pos_x + delta_x
        new_pos_y = self._pos_y + delta_y

        if new_pos_x < self._min_pos_x:
            new_pos_x = self._min_pos_x
        if new_pos_y < self._min_pos_y:
            new_pos_y = self._min_pos_y

        if new_pos_x > self._max_pos_x:
            new_pos_x = self._max_pos_x
        if new_pos_y > self._max_pos_y:
            new_pos_y = self._max_pos_y

        self._pos_x = new_pos_x
        self._pos_y = new_pos_y


    def shoot(self):
        _, end_pos = self.get_pipe_coord()
        self._grenade.shoot(end_pos, self._pipe_angle)
        