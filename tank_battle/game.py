from modules.base import utils
from modules.base import options
from modules.base import translations
from modules.objects import background
from modules.objects import tank
from modules.menu import main_menu
from modules.control import controller
from modules.base import button

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
        self._options = options.Options()
        self._menu = main_menu.MainMenu(screen, self._options)

    def get_options(self):
        return self._options

    def control_tank(self, action, tank):
            if action == 'l':
                tank.move(-5, 0)
            elif action == 'r':
                tank.move(5, 0)
            elif action == 'u':
                tank.pipe_angle(5)
            elif action == 'd':
                tank.pipe_angle(-5)
                

    def loop(self):
        abort = False
        back = background.Background(self._screen)
        back.draw()

        # Musik nur starten, wenn sie nicht läuft
        if self._options.music_enabled():
            pygame.mixer.music.load(utils.get_res_file_path('game_music.mp3'))
            pygame.mixer.music.play(-1)

        ctrl1 = controller.Control(0)
        ctrl2 = controller.Control(1)

        tank1 = tank.Tank(self._screen, init_pos=(0,400), max_pos=(1100, 400), reverse=False)
        tank1.pipe_angle(45)
        tank1.draw()

        tank2 = tank.Tank(self._screen, init_pos=(1100, 400), max_pos=(1100, 400), reverse=True)
        tank2.pipe_angle(45)
        tank2.draw()

        while not abort:
            language = self._options.get_language()
            menu_text = translations.texts[language]["mainmenu"]
            font = utils.get_font(30)
            text_surface = font.render(menu_text, True, "Black")
            button_width = max(200, text_surface.get_width() + 40)

            go_menu = button.Button(
                image=None,
                pos=(button_width // 2 + 40, 40),
                text_input=menu_text,
                font=font,
                base_color="Black",
                hovering_color="Red"
            )

            back.draw()
            mouse_pos = pygame.mouse.get_pos()

            go_menu.change_color(mouse_pos)
            go_menu.update(self._screen)
            
            for e in pygame.event.get():
                if e.type is pygame.QUIT:
                    abort = True
                
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if go_menu.check_for_input(mouse_pos):
                       pygame.mixer.music.stop()
                       return

            self.control_tank(ctrl1.poll(), tank1)
            self.control_tank(ctrl2.poll(), tank2)

            tank1.draw()
            tank2.draw()

            pygame.display.update()
            self._clock.tick(100)


    def run(self):
        self._menu.run()

        while True:
            self.loop()
            self._menu.run()


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Schmatztank Battle")
    
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()
    try:
        game = Game(screen, clock)
        game.run()

    except Exception as e:
        print("Exception occurred: {}".format(e))
        traceback.print_exc()

    pygame.quit()


if __name__ == "__main__":
    main()
