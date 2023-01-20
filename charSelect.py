"""
Gods of Olympus
Last Modified: 1/19/23
Course: CS269
File: titleScreen.py
"""

import pygame
import pygame_gui

class charSelect():

    # Constructor
    def __init__(self, x, y, window_surface, char_image_size):
        self.x = x
        self.y = y
        self.window_surface = window_surface
        self.char_image_size = char_image_size
        self.background = pygame.Surface((self.x, self.y))


    # Adds maps
    def add_maps(self):

        map_size_x = 650
        map_size_y = 400

        map_image = pygame.image.load("Images/logo.png").convert_alpha()
        map_image = pygame.transform.scale(map_image, (map_size_x, map_size_y))
        self.background.blit(map_image, ((self.x - map_size_x) / 2, 0))
        #self.background.blit(map_image, (0, 0))
        self.window_surface.blit(self.background, (0, 0))


    # Adds characters
    def add_characters(self):

        # Make box around characters


        # Import fighter images
        zeus_image = pygame.image.load("Images/zeusmain.png").convert_alpha()
        zeus_image = pygame.transform.scale(zeus_image, (self.char_image_size, self.char_image_size))

        hades_image = pygame.image.load("Images/hadesmain.png").convert_alpha()
        hades_image = pygame.transform.scale(hades_image, (self.char_image_size, self.char_image_size))

        self.background.blit(zeus_image, (-80, self.y / 4))
        self.background.blit(hades_image, (self.x - self.char_image_size + 80, self.y / 4))
        self.window_surface.blit(self.background, (0, 0))


    # Initialize character select
    def initialize_char_select(self):
        pygame.display.set_caption('Character Selection')

        background = pygame.Surface((self.x, self.y))
        sky_image = pygame.image.load("Images/sky.png").convert_alpha()
        background.blit(sky_image, (0, 0))
        self.window_surface.blit(background, (0, 0))

        self.add_characters()
        self.add_maps()


