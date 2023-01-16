"""
Gods of Olympus
Last Modified: 1/6/23
Course: CS269
File: main.py
"""

import pygame
from fighter import Fighter
from pygame.locals import *
import sys

pygame.init()

vec = pygame.math.Vector2

#
HEIGHT = 750
WIDTH = 1300
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gods of Olympus")

# load background image
bg_image = pygame.image.load("Images/OlympusBackground.jpg").convert_alpha()


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# writes in the location of fighters
fighter_1 = Fighter(100, HEIGHT - 50)
fighter_2 = Fighter(WIDTH - 100, HEIGHT - 50)

# game looper
while True:

    # draw background
    draw_bg()

    # move fighters
    fighter_1.move(WIDTH, HEIGHT)
    # fighter_2.move()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # draw hp bar for fighters
    #draw_health_bars(fighter_1.health, 20, 20)  # fighter, x cord., y cord.
    #draw_health_bars(fighter_1.health, WIDTH - (hp_width + 20), 20)

    # allows player to exit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # sets max frame rate
    pygame.display.update()
    FramePerSec.tick(FPS)