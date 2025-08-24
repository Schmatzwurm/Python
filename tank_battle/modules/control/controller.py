from ..base import utils

from . import hand_controllers

import pygame

class Control:
    
    DEFAULT_MAPPINGS = [
        { 
            pygame.K_a: 'l', 
            pygame.K_d: 'r',
            pygame.K_w: 'u',
            pygame.K_s: 'd',
            pygame.K_q: 'shoot',
        },
        { 
            pygame.K_j: 'l', 
            pygame.K_l: 'r',
            pygame.K_i: 'u',
            pygame.K_k: 'd',
            pygame.K_u: 'shoot',
        },
    ]


    def __init__(self, mapping=0):
        self._keys = Control.DEFAULT_MAPPINGS[mapping]


    def poll(self):
        key_events = pygame.key.get_pressed()
        for key in self._keys:
            if key_events[key]:
                return self._keys[key]
        return None
