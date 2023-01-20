"""
Gods of Olympus
Last Modified: 1/20/23
Course: CS269
File: Game.py
"""

import pygame
from pygame import mixer
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
        self.f1_wins = 0
        self.f2_wins = 0
        self.FramePerSec = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # load map
        self.map = Map(1, HEIGHT, WIDTH, ACC, FRIC, FPS, self.screen)

        #define fighter variables
        self.ledges = self.map.draw_ledges()

        # starting location of fighters
        self.fighter_1 = Zeus(1, 0, HEIGHT - 200, self.ledges, self.screen)
        self.fighter_2 = Zeus(2, WIDTH - 400, HEIGHT-500, self.ledges, self.screen)


    # Runs the game
    def runGame(self):

        # Sets screen header
        pygame.display.set_caption("Gods of Olympus")

        # Load music
        mixer.music.load('sound_1.wav')
        mixer.music.play(-1)

        # Draws scoreboard    
        self.map.draw_stats(self.f1_wins, self.f2_wins)

        # game looper
        while True:

            # checks if a fighter has no hp and restarts the game if that's the case
            if self.fighter_1.health <= 0 or self.fighter_2.health <= 0:
                if self.fighter_1.health <= 0:
                    self.f2_wins += 1     # fighter 2 earns a round
                else:
                    self.f1_wins += 1     # fighter 1 earns a round
                pygame.time.wait(1500)
                self.runGame()

            # draw background
            self.map.draw_bg()
            self.ledges = self.map.draw_ledges()

            # move fighters
            self.fighter_1.move(self.WIDTH, self.HEIGHT, self.fighter_2, self.screen, self.ledges)
            self.fighter_2.move(self.WIDTH, self.HEIGHT, self.fighter_1, self.screen, self.ledges)

            # draw fighters
            self.fighter_1.update()
            self.fighter_2.update()
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