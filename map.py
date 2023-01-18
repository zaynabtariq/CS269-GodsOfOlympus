"""
Gods of Olympus
Last Modified: 1/15/23 by zaynab
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
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.bg_image, (self.WIDTH, self.HEIGHT))

        self.screen.fill((0,0,0))
        self.screen.blit(scaled_bg, (self.scroll, 0))

        self.screen.blit(scaled_bg, (self.WIDTH+self.scroll,0))

        if self.scroll  == -self.WIDTH:
            self.screen.blit(scaled_bg, (self.WIDTH+self.scroll,0) )
            self.scroll = 0

        self.scroll -= 1

    # draws health bars
    def draw_health_bars(self, health, x, y, screen):
        ratio = health / 100
        pygame.draw.rect(screen, (255, 255, 255), (x -2, y-2, 404, 34))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, 400, 30))
        pygame.draw.rect(screen, (255, 255, 0), (x, y, 400 * ratio, 30))