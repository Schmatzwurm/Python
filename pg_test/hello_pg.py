import os
import pygame

def load_image(file_name):
    base_dir_path = os.path.split(os.path.abspath(__file__))[0]
    file_path = os.path.join(base_dir_path, "res", file_name)
    return pygame.image.load(file_path).convert()

def main():
    pygame.init()
    pygame.display.set_caption("Schmatzwurmgame")
    clock = pygame.Clock()
    screen = pygame.display.set_mode((480, 340))
    background_color = (255, 255, 128)
    screen.fill(background_color)

    screen_rect = screen.get_rect()
    center_coords = pygame.Vector2(screen_rect.center)

    running = True
    while running:
        screen.fill(background_color)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(100)
    pygame.quit()

if __name__ == "__main__":
    main()
