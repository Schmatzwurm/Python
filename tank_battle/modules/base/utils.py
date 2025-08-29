import os
import pygame

def get_res_file_path(file_name):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, '..', '..', 'resources', file_name)

    return file_path


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(get_res_file_path('font.ttf'), size)


def saturate(values, min_values, max_values):
    saturated = []
    for i in range(len(values)):
        saturated.append(max(min_values[i], min(max_values[i], values[i])))
    return saturated
