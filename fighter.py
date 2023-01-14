"""
Gods of Olympus
Last Modified: 1/14/23
Course: CS269
File: fighter.py
"""

import pygame

class Fighter():
    def __init__(self, player, x, y):
        self.flip = False #used to make sure the character is always facing the opponent
        self.player = player
        self.rect = pygame.Rect((x, y, 50, 100))
        self.vel_y = 0
        self.jump = False
        self.attack_type = 0
        self.health = 100
    
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
        
            #attacks
            if key[pygame.K_c] or key[pygame.K_v] or key[pygame.K_b]:
                if key[pygame.K_c]:
                    self.attack_type = 1
                    self.attack(screen, target)
                if key[pygame.K_v]:
                    self.attack_type = 2
                    self.attack(screen, target)
                if key[pygame.K_b]:
                    self.attack_type = 3
                    self.attack(screen, target)
                    
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

            #attacks
            if key[pygame.K_COMMA] or key[pygame.K_PERIOD] or key[pygame.K_SLASH]:
                if key[pygame.K_COMMA]:
                    self.attack_type = 1
                    self.attack(screen, target)
                if key[pygame.K_PERIOD]:
                    self.attack_type = 2
                    self.attack(screen, target)
                if key[pygame.K_SLASH]:
                    self.attack_type = 3
                    self.attack(screen, target)

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
            
        #ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True


        #update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    
