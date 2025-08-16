import modules

from modules.objects import background
from modules.objects import tank

import pygame
import traceback

from pygame import display

# Must come from options later
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:
    def __init__(self, screen, clock):
        self._screen = screen
        self._clock = clock

    def loop(self):
        abort = False
        back = background.Background(self._screen)
        back.draw()

        t1 = tank.Tank(self._screen)
        t1.draw(0, 0)

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
    #screen.get_height
    game = Game(screen, clock)

    try:
        game.loop()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        traceback.print_exc()

    pygame.quit()

if __name__ == "__main__":
    main()
