"""
Gods of Olympus
Last Modified: 1/6/23
Course: CS269
File: fighter.py
"""

import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 50, 100))
        self.vel_y = 0
        self.jump = False
    
    def move(self, WIDTH, HEIGHT):
        SPEED = 10
        GRAVITY = 1.5
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #movement
        #check player 1 controls
        if self.player == 1:
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            #jump
            if key[pygame.K_w] and self.jump == False:
                self.jump = True
                self.vel_y = -30
        
        #check player 2 controls
        if self.player == 2:
            if key[pygame.K_LEFT]:
                dx = -SPEED
            if key[pygame.K_RIGHT]:
                dx = SPEED
            #jump
            if key[pygame.K_UP] and self.jump == False:
                self.jump = True
                self.vel_y = -30

        #apply gravity
        if self.rect.y < HEIGHT - 50:
            self.vel_y += GRAVITY

        dy += self.vel_y

        #ensures the player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right
        if self.rect.bottom + dy > HEIGHT: # write - X if there is a floor
            self.vel_y = 0
            self.jump = False
            dy = HEIGHT - self.rect.bottom # write - X if there is a floor


        #update player position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    
