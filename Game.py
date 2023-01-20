"""
Gods of Olympus
Last Modified: 1/19/23
Course: CS269
File: Game.py
"""

import pygame
from pygame import mixer
from fighter import Fighter
from Zeus import Zeus
# from Hades import Hades
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

        # Load music
        mixer.music.load('sound_1.wav')
        mixer.music.play(-1)

        # game looper
        while True:

            # checks if a fighter has no hp and restarts the game if that's the case
            if self.fighter_1.health <= 0 or self.fighter_2.health <= 0:
                pygame.time.wait(1500)
                self.runGame()

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
            self.map.draw_health_bars(self.fighter_1.health, 'fighter_2')
            self.map.draw_health_bars(self.fighter_2.health, 'fighter_1')
            self.map.draw_score_icons() # draw icons of idols

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
