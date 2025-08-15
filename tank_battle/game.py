import base
import control
import physics

import pygame
import time

from pygame import display
from base import utils

# Must come from options later
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:
    def __init__(self, screen, clock):
        self._screen = screen
        self._clock = clock
        background_image = pygame.image.load(file=utils.get_res_file_path('landscape.jpg'))
        screen.blit(background_image, (0,0)) 

    def loop(self):
        abort = False

        while not abort:
            pygame.display.update()
            self._clock.tick(100)


def main():
    pygame.init()
    pygame.display.set_caption("Schmatzpanzer Battle")
    
    clock = pygame.Clock()
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Game(screen, clock)

    try:
        game.loop()
    except:
        pass
    pass

    pygame.quit()

if __name__ == "__main__":
    main()
