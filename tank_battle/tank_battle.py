import os
import pygame

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)



def main():
    pygame.init()
    pygame.display.set_caption("Schmatzpanzer Battle")
    clock = pygame.Clock()
    screen = pygame.display.set_mode((1763, 980))
    background = pygame.image.load(file="{}/resources/landscape.jpg".format(script_dir))
    screen.blit(background, (0,0))
   
    class Tank:
        def __init__(self):
            image = pygame.image.load(file="{}/resources/tank.png".format(script_dir))
            self.image_right = pygame.transform.scale(image, (180, 150))
            self.image_left = pygame.transform.flip(self.image_right, True, False)
            self.image = self.image_right
            

        def draw(self, x, y):
            screen.blit(self.image, (x, y))
 

    tank = Tank()
    tank_x = 50
    tank_y = 600
    
    

    running = True
    while running:
        screen.blit(background, (0,0)) # übermalen
        tank.draw(tank_x, tank_y)

        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
          
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            tank_x -= 5
            tank.image = tank.image_left
             
            
        if keys[pygame.K_d]:
            tank_x += 5
            tank.image = tank.image_right
            

        if tank_x < 0:
                tank_x = 0
        elif tank_x > 1600:
                tank_x = 1600

        
        


        pygame.display.update()
        clock.tick(100)
    pygame.quit()

if __name__ == "__main__":
    main()