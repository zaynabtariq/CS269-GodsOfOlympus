"""
Gods of Olympus
Last Modified: 1/11/23 by jctjad
Course: CS269
File: map.py
"""

import pygame

class Map():
    # Constructor
    def __init__(self, HEIGHT, WIDTH, ACC, FRIC, FPS, screen):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.ACC = ACC
        self.fRIC = FRIC
        self.FPS = FPS

        # Set screen up
        self.screen = screen
        pygame.display.set_caption("Gods of Olympus")

        # Load background
        self.bg_image = pygame.image.load("OlympusBackground.jpg").convert_alpha()
        
        #scoreboard
        outer_scoreboard = pygame.image.load("Images/scoreboard.jpg").convert_alpha()
        inner_scoreboard = pygame.image.load("Images/inner_scoreboard.jpg").convert_alpha()
        
        #width of hp bars
        hp_width = 500
    
    def draw_ledges(self):
        ledge_1_rect = pygame.Rect((150, self.HEIGHT - 100, 200, 15))  # (left, top), (width, height)
        ledge_1 = pygame.image.load( "platform1.png" ).convert_alpha()
        ledge_1_scaled = pygame.transform.scale(ledge_1, (200, 180))
        self.screen.blit(ledge_1_scaled, (150, 410))

        return ledge_1, ledge_1_rect

    # Methods
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.bg_image, (self.WIDTH, self.HEIGHT))
        self.screen.blit(scaled_bg, (0,0))
        
    #draws the two scoreboards
    def draw_health_bars(health, x, y):
        #inner scoreboard
        scaled_isb = pygame.transform.scale(inner_scoreboard, (1000, 50))
        screen.blit(scaled_isb, (150,30))    

        #outer scoreboard
        scaled_osb = pygame.transform.scale(outer_scoreboard, (1000, 50))
        screen.blit(scaled_osb, (150,30))
