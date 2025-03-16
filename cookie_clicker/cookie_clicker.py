# Cash Clicker
# made by Schmatzwurm

import pygame, sys, time

class Game:
    def __init__(self):
        self.cookies = 0
        self.cookie_per_click = 1
        self.auto_clicker_amount = 0
        self.cookie = pygame.Rect(400 - 150, 300 - 150, 300, 300 )
        self.cookie_color = "#522920"
        self.clicked = False

        self.upgradeBtn = pygame.Rect(10, 50, 185, 75)
        self.upgrade1_cost = 15

        self.upgradeBtn2 = pygame.Rect(10, 190, 185, 75)
        self.upgrade2_cost = 40

        self.game_font = pygame.font.Font(None, 28)

    def upgrade(self):
        self.upgrade1_description = self.game_font.render(f"+{self.cookie_per_click} cookie per click.", True, "#ffffff")
        self.display_cost = text_font.render(f"Cost: {self.upgrade1_cost}", True, "#ffffff")

        self.upgrade2_description = self.game_font.render(f"+{self.auto_clicker_amount} cookie per sec.", True, "#ffffff")
        self.display_cost2 = text_font.render(f"Cost: {self.upgrade2_cost}", True, "#ffffff")


        pygame.draw.rect(screen, "#488ebd", self.upgradeBtn, border_radius=15)
        screen.blit(self.display_cost, (15, 85))
        screen.blit(self.upgrade1_description,(15, 55))

        pygame.draw.rect(screen, "#488ebd", self.upgradeBtn2, border_radius=15)
        screen.blit(self.display_cost2, (15, 220))
        screen.blit(self.upgrade2_description,(15, 190))

    def draw_score(self):
        self.display_cookies = text_font.render(f"Cookies: {str(self.cookies)}", True, "#ffffff")
        screen.blit(self.display_cookies, (0, 565))

    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:            
                self.clicked = True
            else:
                if self.clicked:
                    click_sound.play()
                    self.cookies += self.cookie_per_click
                    self.clicked = False

        if self.upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:                  
                    if self.cookies >= self.upgrade1_cost:                   
                        self.cookies -= self.upgrade1_cost
                        self.upgrade1_cost *= 2
                        self.cookie_per_click += 2
                    click_sound.play()
                    self.clicked = False

        if self.upgradeBtn2.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:                  
                    if self.cookies >= self.upgrade2_cost:                   
                        self.cookies -= self.upgrade2_cost
                        self.upgrade2_cost *= 3
                        self.auto_clicker_amount += 1 
                        while self.auto_clicker_amount >= 1:
                            self.add_autoclicks                              
                              
                    click_sound.play()
                    self.clicked = False
        
        pygame.draw.rect(screen, self.cookie_color, self.cookie,border_radius=150)
        
    def add_autoclicks(self):
        if game.auto_clicker_amount >=1:
            self.cookies += self.auto_clicker_amount
            time.sleep(1)

        
    def render(self):
        self.click_button()
        self.draw_score()
        self.upgrade()
        

pygame.init()

width = 800
height = 600

game = Game()

screen = pygame.display.set_mode(size=(width,height))
windowSurface = pygame.display.set_caption("Cash-Clicker")

text_font = pygame.font.Font(None,50)
title = text_font.render("Cash Clicker", True, "#000000")
background = pygame.image.load("background.png").convert()
click_sound = pygame.mixer.Sound("Mouse.mp3")
clock = pygame.time.Clock()

#for game.auto_clicker_amount

while True:
    screen.blit(background,(0, 0))
    game.add_autoclicks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(title, (300, 15))

    game.render()

    pygame.display.update()
    clock.tick(60)
