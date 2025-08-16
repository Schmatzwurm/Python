import os
import pygame
from tank_battle.base.button import Button
from tank_battle.old.main import *


script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)



def main():
    pygame.init()
    pygame.display.set_caption("Schmatzpanzer Battle")
    clock = pygame.Clock()
    screen = pygame.display.set_mode((1280, 720))
    background = pygame.image.load(file="{}/resources/landscape.jpg".format(script_dir))
    background = pygame.transform.scale(background, (1280, 720))
    screen.blit(background, (0,0))
    
   
    class Tank:
        def __init__(self, inverted=False):
            image = pygame.image.load(file="{}/resources/tank.png".format(script_dir))
            self._image_right = pygame.transform.scale(image, (180, 150))
            self._image_left = pygame.transform.flip(self._image_right, True, False)
            self._image = self._image_right
            self._inverted = inverted
                  

        def draw(self, x, y):
            screen.blit(self.image, (x, y))
 

    tank = Tank()
    tank_x = 50
    tank_y = 400
    
    

    running = True
    while running:
        from tank_battle.old.main import get_font, main_menu
        screen.blit(background, (0,0)) # übermalen
        tank.draw(tank_x, tank_y)

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # BACK-Button links unten
        from tank_battle.old.main import get_font, main_menu
        GAME_BACK = Button(
            image=None,
            pos=(120, 50),  # Linke untere Ecke
            text_input="BACK",
            font=get_font(50),
            base_color="Black",
            hovering_color="Red"
        )
        GAME_BACK.changeColor(OPTIONS_MOUSE_POS)
        GAME_BACK.update(screen)

        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if GAME_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    return  # Wichtig: Schleife verlassen

            
          
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            tank_x -= 5
            tank.image = tank.image_left
             
            
        if keys[pygame.K_d]:
            tank_x += 5
            tank.image = tank.image_right
            

        if tank_x < 0:
                tank_x = 0
        elif tank_x > 1100:
                tank_x = 1100

        pygame.display.update()
        clock.tick(100)
    pygame.quit()

