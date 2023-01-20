"""
Gods of Olympus
Last Modified: 1/19/23 
Course: CS269
File: map.py
"""

import pygame


class Map():
    # Constructor
    def __init__(self, num, HEIGHT, WIDTH, ACC, FRIC, FPS, screen):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.ACC = ACC
        self.fRIC = FRIC
        self.FPS = FPS
        self.num = num

        # Set screen up
        self.screen = screen
        # pygame.display.set_caption("Gods of Olympus")

        # Load background
        if self.num == 1:
            self.bg_image = pygame.image.load("Images/skybackground_2.png").convert_alpha()
        elif self.num == 2:
            self.bg_image = pygame.image.load("Images/sky.png").convert_alpha()
        elif self.num == 3:
            self.bg_image = pygame.image.load("Images/sky.png").convert_alpha()

    # colors
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    # width of hp bars
    hp_width = 500

    # scroll indicator
    scroll = 0

    def draw_ledges(self):
         if self.num == 1:
            ledge_1_rect = pygame.Rect((155, self.HEIGHT - 300, 260, 40))  # (left, top), (width, height)
            ledge_1 = pygame.image.load("Images/sky_platform.png").convert_alpha()
            ledge_1_scaled = pygame.transform.scale(ledge_1, (300, 100))
            self.screen.blit(ledge_1_scaled, (150, 410))


            ledge_2_rect = pygame.Rect((self.WIDTH - 485, self.HEIGHT - 350, 255, 40))  # (left, top), (width, height)
            ledge_2 = pygame.image.load("Images/sky_platform.png").convert_alpha()
            ledge_2_scaled = pygame.transform.scale(ledge_2, (300, 100))
            self.screen.blit(ledge_2_scaled, (self.WIDTH - 500, 360))


            return ledge_1_rect, ledge_2_rect

    # Methods
    def draw_bg(self, screen):

        scaled_bg = pygame.transform.scale(self.bg_image, (self.WIDTH, self.HEIGHT))

        self.screen.fill((0, 0, 0))
        self.screen.blit(scaled_bg, (self.scroll, 0))

        self.screen.blit(scaled_bg, (self.WIDTH + self.scroll, 0))

        if self.scroll == -self.WIDTH:
            self.screen.blit(scaled_bg, (self.WIDTH + self.scroll, 0))
            self.scroll = 0

        self.scroll -= 1

        ground = pygame.image.load("Images/sky_floor.png").convert_alpha()
        ground_scaled = pygame.transform.scale(ground, (self.WIDTH + 10, 110))
        self.screen.blit(ground_scaled, (0, self.HEIGHT -110))


    # draw icons next to scoreboard

    def draw_score_icons(self, screen):
        fighter1_icon = pygame.image.load("Images/Icons_Zeus.png")
        screen.blit(fighter1_icon, (30,30))

        fighter2_icon = pygame.image.load("Images/Icons_Hades.png")
        screen.blit(fighter2_icon, (1170,30))


    # draws health bars

    def draw_health_bars(self, health, screen, player):
        ratio = health / 100
        '''pygame.draw.rect(screen, (255, 255, 255), (x -2, y-2, 404, 34))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, 400, 30))
        pygame.draw.rect(screen, (255, 255, 0), (x, y, 400 * ratio, 30))'''
        #scoreboards
        if player == 'fighter_2':
            left_blue_inner = pygame.image.load("Images/left_blue_inner.jpg").convert_alpha()
            scaled_isb2 = pygame.transform.scale(left_blue_inner, (400, 50))
            screen.blit(scaled_isb2, (150,60))
            left_green_outer = pygame.image.load("Images/left_green_outer.jpg").convert_alpha()
            scaled_osb = pygame.transform.scale(left_green_outer, (400 * ratio, 50))
            screen.blit(scaled_osb, (150 + (400 - 400 * ratio),60))

        if player == 'fighter_1':
            right_red_inner = pygame.image.load("Images/right_red_inner.jpg").convert_alpha()
            scaled_isb = pygame.transform.scale(right_red_inner, (400, 50))
            screen.blit(scaled_isb, (750,60))
            right_purple_outer = pygame.image.load("Images/right_purple_outer.jpg").convert_alpha()
            scaled_osb2 = pygame.transform.scale(right_purple_outer, (400 * ratio, 50))
            screen.blit(scaled_osb2, (750, 60))
