import pygame
import math

from ..base import utils

class Tank:
    def __init__(self, screen, size=(180, 150), 
                 init_pos=(0,0), min_pos=(0,0), max_pos=(100,100), 
                 reverse=False):
        image_file_path = utils.get_res_file_path('tank.png')
        image = pygame.image.load(image_file_path)
        self._image_right = pygame.transform.scale(image, size)
        self._image_left = pygame.transform.flip(self._image_right, True, False)
        if reverse:
            self._image = self._image_left
        else:
            self._image = self._image_right
        self._screen = screen
        self._reverse = reverse
        self._pos_x = init_pos[0]
        self._pos_y = init_pos[1]
        self._min_pos_x = min_pos[0]
        self._min_pos_y = min_pos[1]
        self._max_pos_x = max_pos[0]
        self._max_pos_y = max_pos[1]
        self._pipe_angle = 0
        self._pipe_length = 70


    def draw(self):
        self._screen.blit(self._image, (self._pos_x, self._pos_y))
        start_pos_y = self._pos_y + 62
        if self._reverse:
            start_pos_x = self._pos_x + 72
            actual_angle = 180 + self._pipe_angle
        else:
            start_pos_x = self._pos_x + 105
            actual_angle = - self._pipe_angle

        angle_rad = math.radians(actual_angle)    
        end_pos = (
            start_pos_x + self._pipe_length * math.cos(angle_rad),
            start_pos_y + self._pipe_length * math.sin(angle_rad)
        )
        start_pos = (start_pos_x, start_pos_y)
        pygame.draw.line(self._screen, (0, 0, 0), start_pos, end_pos, 10)


    def pipe_angle(self, delta_angle):
        new_angle = self._pipe_angle + delta_angle
        if new_angle < 0:
            new_angle = 0
        elif new_angle > 90:
            new_angle = 90
        self._pipe_angle = new_angle


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
    