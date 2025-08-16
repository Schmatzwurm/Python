import modules
from modules.base import utils
from modules.objects import background
from modules.objects import tank
from modules.menu import main_menu

import pygame
import traceback

from pygame import display

# Must come from options later
# Also calculate all positions based on screen dimension later
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

        # Musik nur starten, wenn sie nicht läuft
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(utils.get_res_file_path('game_music.mp3'))
            pygame.mixer.music.play(-1)

        t1 = tank.Tank(self._screen, init_pos=(0,400), max_pos=(1100, 400), reverse=False)
        t1.pipe_angle(60)
        t1.draw()

        t2 = tank.Tank(self._screen, init_pos=(1100, 400), max_pos=(1100, 400), reverse=True)
        t2.pipe_angle(30)
        t2.draw()

        while not abort:
            back.draw()
            
            for e in pygame.event.get():
                if e.type is pygame.QUIT:
                    abort = True

            t1.move(5, 0)
            t1.draw()
            t2.move(5, 0)
            t2.draw()
            pygame.display.update()
            self._clock.tick(100)


def main():
    pygame.init()
    pygame.display.set_caption("Schmatzpanzer Battle")
    
    clock = pygame.Clock()
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #screen.get_height
    menu = main_menu.Menu(screen)
    menu.run()      # Menü anzeigen, bis Play gedrückt wird

    game = Game(screen, clock)

    try:
        game.loop()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        traceback.print_exc()

    pygame.quit()

if __name__ == "__main__":
    main()
