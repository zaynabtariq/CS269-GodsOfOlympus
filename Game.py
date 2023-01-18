"""
Gods of Olympus
Last Modified: 1/18/23 by zaynab
Course: CS269
File: Game.py
"""

import pygame
from pygame import mixer
from fighter import Fighter
from Zeus import Zeus
from Hades import Hades
from map import Map
#from background import Background
from pygame.locals import *
import sys

pygame.init()


HEIGHT = 750
WIDTH = 1300
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()

mixer.music.load('sound_1.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gods of Olympus")

# load map
map = Map(1, HEIGHT, WIDTH, ACC, FRIC, FPS, screen)

#define fighter variables

ledges = map.draw_ledges()
# starting location of fighters
fighter_1 = Zeus(1, 0, HEIGHT-200, ledges, screen)
fighter_2 = Zeus(2, WIDTH - 10, HEIGHT-500, ledges, screen)


# game looper
while True:

    # draw background
    map.draw_bg(screen)
    ledges = map.draw_ledges()


    # move fighters
    fighter_1.move(WIDTH, HEIGHT, fighter_2, screen, ledges)
    fighter_2.move(WIDTH, HEIGHT, fighter_1, screen, ledges)

    # draw fighters
    fighter_1.update()
    fighter_2.update()
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # draw hp bar for fighters
    '''map.draw_health_bars(fighter_1.health, 20, 20, screen)  # fighter, x cord., y cord.
    map.draw_health_bars(fighter_2.health, WIDTH - (400 + 20), 20, screen)'''
    map.draw_health_bars(fighter_1.health, screen, 'fighter_2')  # fighter, x cord., y cord., player
    map.draw_health_bars(fighter_2.health, screen, 'fighter_1')

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
    FramePerSec.tick(FPS)
