import modules

import pygame
import time

from pygame import display
from modules.base import utils
from modules.objects import tank
from modules.objects import background

# Must come from options later
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:
    def __init__(self, screen, clock):
        self._screen = screen
        self._clock = clock

    def loop(self):
        abort = False
        background = background.Background(self._screen)
        background.draw()

        tank = tank.Tank(self._screen)

        while not abort:
            for e in pygame.event.get():
                if e.type is pygame.QUIT:
                    abort = True
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
