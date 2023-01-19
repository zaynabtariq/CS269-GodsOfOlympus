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
 
#def colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

hp_width = 500

#load background image
bg_image = pygame.image.load("Images/olympus_background.jpg").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    screen.blit(scaled_bg, (0,0))

def draw_health_bars(health, x, y):
    pygame.draw.rect(screen, YELLOW, (x, y, hp_width, 30))

#writes in the location of fighters
fighter_1 = Fighter(1, 100, HEIGHT - 50)
fighter_2 = Fighter(2, WIDTH - 100, HEIGHT - 50)

#game looper
while True:
    
    #draw background
    draw_bg()

    #move fighters 
    fighter_1.move(WIDTH, HEIGHT, screen, fighter_2)
    fighter_2.move(WIDTH, HEIGHT, screen, fighter_1)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #draw fighter stats
    draw_health_bars(fighter_1.health, 20, 20)
    draw_health_bars(fighter_1.health, WIDTH - (hp_width + 20), 20)


    #allows player to exit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #sets max frame rate
    pygame.display.update()
    FramePerSec.tick(FPS)
