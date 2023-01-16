"""
Gods of Olympus
Last Modified: 1/15/23 by zaynab
Course: CS269
File: Game.py
"""

import pygame
from fighter import Fighter
from Zeus import Zeus
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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gods of Olympus")

# load map
map = Map(1, HEIGHT, WIDTH, ACC, FRIC, FPS, screen)

#define fighter variables

ledges = map.draw_ledges()
# starting location of fighters
fighter_1 = Fighter(1, 100, HEIGHT-200, ledges)
fighter_2 = Fighter(2, WIDTH - 100, HEIGHT-500, ledges)


# game looper
while True:

    # draw background
    map.draw_bg()
    ledges = map.draw_ledges()


    # move fighters
    fighter_1.move(WIDTH, HEIGHT, fighter_2, screen, ledges)
    fighter_2.move(WIDTH, HEIGHT, fighter_1, screen, ledges)

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # draw hp bar for fighters
    map.draw_health_bars(fighter_1.health, 20, 20, screen)  # fighter, x cord., y cord.
    map.draw_health_bars(fighter_2.health, WIDTH - (400 + 20), 20, screen)

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



