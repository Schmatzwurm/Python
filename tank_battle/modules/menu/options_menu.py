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
        self._fs_on = False
        self._lng_ws = False
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

        if self._fs_on:
            pygame.display.set_mode(self._screen.get_size(), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode(self._screen.get_size())
        
    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._screen.fill("white")

            options_title = utils.texts[utils.language]["options"]
            music_text = utils.texts[utils.language]["music"]
            fullscreen_text = utils.texts[utils.language]["fullscreen"]
            language_text = utils.texts[utils.language]["language"]
            back_text = utils.texts[utils.language]["back"]
            on_value = utils.texts[utils.language]["on"]
            off_value = utils.texts[utils.language]["off"]



            # Options Überschrift
            text = Menu.get_font(55).render(options_title, True, "Black")
            rect = text.get_rect(center=(640, 60))
            self._screen.blit(text, rect)

            # Music
            text = Menu.get_font(40).render(music_text, True, "Black")
            rect = text.get_rect(center=(530, 250))
            self._screen.blit(text, rect)

            # Fullscreen
            text = Menu.get_font(40).render(fullscreen_text, True, "Black")
            rect = text.get_rect(center=(430, 350))
            self._screen.blit(text, rect)

            # Sprache
            text = Menu.get_font(40).render(language_text, True, "Black")
            rect = text.get_rect(center=(470, 450))
            self._screen.blit(text, rect)

            pygame.draw.line(self._screen, "Black", (200, 300), (1000, 300), 3)
            pygame.draw.line(self._screen, "Black", (200, 400), (1000, 400), 3)
            
            # Zurück Button
            back = button.Button(image=None, pos=(150, 50), 
                                 text_input=back_text, font=Menu.get_font(40), base_color="Black", hovering_color="Red")
            back.change_color(mouse_pos)
            back.update(self._screen)

            # Music Button on/off
            music_value = on_value if self._music_on else off_value
            color = "Green" if self._music_on else "Red"
            h_color = "Green" if self._music_on else "Red"
            on_or_off = button.Button(image=None, pos=(750, 250), 
                                 text_input=music_value, font=Menu.get_font(40), base_color=color, hovering_color=h_color)
            on_or_off.change_color(mouse_pos)
            on_or_off.update(self._screen)

            # Fullscreen Button
            fs_value = "[X]" if self._fs_on else "[ ]"
            fs_btn = button.Button(image=None, pos=(750, 350), 
                                 text_input=fs_value, font=Menu.get_font(40), base_color="Black", hovering_color=False)
            fs_btn.change_color(mouse_pos)
            fs_btn.update(self._screen)

            # Language Button
            lng_text = "DEUTSCH" if self._lng_ws else "ENGLISH"
            lng_btn = button.Button(image=None, pos=(800, 450), 
                                 text_input=lng_text, font=Menu.get_font(40), base_color="Black", hovering_color=False)
            lng_btn.change_color(mouse_pos)
            lng_btn.update(self._screen)


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

                    if fs_btn.check_for_input(mouse_pos):
                        self._fs_on = not self._fs_on
                        self.apply()

                    if lng_btn.check_for_input(mouse_pos):
                        utils.language = "en" if utils.language == "de" else "de"
                        self._lng_ws = not self._lng_ws
                        

            pygame.display.update()
