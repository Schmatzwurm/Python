import pygame

import utils

class Tank:
    def __init__(self, screen):
        base_dir = utils.get_base_dir()
        image = pygame.image.load(file="{}/resources/tank.png".format(base_dir))
        self.image_right = pygame.transform.scale(image, (180, 150))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.screen = screen
        

    def draw(self, x, y):
        self.screen.blit(self.image, (x, y))


    