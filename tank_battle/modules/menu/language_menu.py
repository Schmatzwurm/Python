from .base_menu import BaseMenu

from ..base import utils
from ..base import button
from ..base import translations

import pygame
import sys


class LanguageMenu(BaseMenu):
    def __init__(self, screen, options):
        super().__init__(screen, options)

    def run(self):
        languages = [("de", "DEUTSCH"), ("en", "ENGLISH"), ("es", "ESPAÑOL"), ("fr", "FRANÇAIS")]
        
        while True:
            language = self._options.get_language()
            choose_language_text = translations.texts[language]["choose language"]
            back_text = translations.texts[translations.language]["back"]
            self._screen.fill("white")
            title = utils.get_font(50).render(choose_language_text, True, "Black")
            self._screen.blit(title, title.get_rect(center=(640, 100)))

            buttons = []
            for i, (code, name) in enumerate(languages):
                btn = button.Button(
                    image=None,
                    pos=(640, 220 + i*80),
                    text_input=name,
                    font=utils.get_font(40),
                    base_color="Black",
                    hovering_color="Red"
                )
                btn.change_color(pygame.mouse.get_pos())
                btn.update(self._screen)
                buttons.append((btn, code))

            # Back button
            back_btn = button.Button(
                image=None,
                pos=(150, 50),
                text_input=back_text,
                font=utils.get_font(40),
                base_color="Black",
                hovering_color="Red"
            )

            back_btn.change_color(pygame.mouse.get_pos())
            back_btn.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_btn.check_for_input(pygame.mouse.get_pos()):
                        return
                    for btn, code in buttons:
                        if btn.check_for_input(pygame.mouse.get_pos()):
                            self._options.set_language(code)
                            return

            pygame.display.update()
