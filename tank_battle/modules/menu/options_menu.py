from ..base import utils
import game
import pygame
import sys
from ..base import button

pygame.init()
pygame.mixer.init()

class Menu:
    def __init__(self, screen):
        image_file_path = utils.get_res_file_path('menu_bg.jpg')
        image = pygame.image.load(image_file_path)
        self._background_image = pygame.transform.scale(image, screen.get_size())
        self._screen = screen
        self._music_on = True

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(utils.get_res_file_path('font.ttf'), size)
    
    def get_music_on(self):
        return self._music_on
    
    def apply(self):
        if not self._music_on:
            pygame.mixer.music.stop()
        else:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
        
    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._screen.fill("white")

            text = Menu.get_font(55).render("OPTIONS", True, "Black")
            rect = text.get_rect(center=(640, 60))
            self._screen.blit(text, rect)

            text = Menu.get_font(40).render("MUSIC:", True, "Black")
            rect = text.get_rect(center=(400, 250))
            self._screen.blit(text, rect)

            back = button.Button(image=None, pos=(110, 50), 
                                 text_input="BACK", font=Menu.get_font(40), base_color="Black", hovering_color="Red")
            back.change_color(mouse_pos)
            back.update(self._screen)

            # Button-Text je nach Status
            music_text = "ON" if self._music_on else "OFF"
            color = "Green" if self._music_on else "Red"
            h_color = "Green" if self._music_on else "Red"
            on_or_off = button.Button(image=None, pos=(600, 250), 
                                 text_input=music_text, font=Menu.get_font(40), base_color=color, hovering_color=h_color)
            on_or_off.change_color(mouse_pos)
            on_or_off.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back.check_for_input(mouse_pos):
                        return 

                    if on_or_off.check_for_input(mouse_pos):
                        self._music_on = not self._music_on  # Status umschalten
                        self.apply()

            pygame.display.update()
