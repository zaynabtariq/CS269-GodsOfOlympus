"""
Gods of Olympus
Last Modified: 1/19/23
Course: CS269
File: freeplay.py
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



# starting location of fighters
fighter = Fighter(1, 100, HEIGHT-200)
enemy = Fighter(2, WIDTH - 100, HEIGHT-200)


# game looper
while True:

    # draw background
    map.draw_bg()
    map.draw_ledges()


    # move fighters
    fighter.move(WIDTH, HEIGHT, enemy, screen)



    # draw fighters
    fighter.draw(screen)
    enemy.draw(screen)

    # draw hp bar for fighters
    map.draw_health_bars(fighter.health, 20, 20, screen)  # fighter, x cord., y cord.
    map.draw_health_bars(enemy.health, WIDTH - (400 + 20), 20, screen)

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
