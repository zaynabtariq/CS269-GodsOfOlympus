"""
Gods of Olympus
Last Modified: 1/17/23
Course: CS269
File: Game.py
"""

import pygame
from fighter import Fighter
from Zeus import Zeus
from map import Map
from pygame.locals import *
import sys

class Game():

    # Constructor
    def __init__(self, HEIGHT, WIDTH, ACC, FRIC, FPS):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.ACC = ACC
        self.FRIC = FRIC
        self.FPS = FPS
        self.FramePerSec = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # load map
        self.map = Map(1, HEIGHT, WIDTH, ACC, FRIC, FPS, self.screen)

        #define fighter variables
        self.ledges = self.map.draw_ledges()

        # starting location of fighters
        self.fighter_1 = Fighter(1, 100, self.HEIGHT-200, self.screen, self.ledges)
        self.fighter_2 = Fighter(2, self.WIDTH - 100, self.HEIGHT-500, self.screen, self.ledges)


    # Runs the game
    def runGame(self):
        pygame.display.set_caption("Gods of Olympus")

        # game looper
        while True:

            # draw background
            self.map.draw_bg()
            self.ledges = self.map.draw_ledges()

            # move fighters
            self.fighter_1.move(self.WIDTH, self.HEIGHT, self.fighter_2, self.screen, self.ledges)
            self.fighter_2.move(self.WIDTH, self.HEIGHT, self.fighter_1, self.screen, self.ledges)

            # draw fighters
            self.fighter_1.draw(self.screen)
            self.fighter_2.draw(self.screen)

            # draw hp bar for fighters
            self.map.draw_health_bars(self.fighter_1.health, 20, 20, self.screen)  # fighter, x cord., y cord.
            self.map.draw_health_bars(self.fighter_2.health, self.WIDTH - (400 + 20), 20, self.screen)

            # allows player to exit
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            # sets max frame rate
            pygame.display.update()
            self.FramePerSec.tick(self.FPS)
