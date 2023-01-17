"""
Gods of Olympus
Last Modified: 1/6/23
Course: CS269
File: fighter.py
"""
import pygame
from fighter import Fighter

class Zeus(Fighter):
    def __init__(self, player, x, y):
        super().__init__(player, x, y)
        self.x = x
        self.y = y
        self.animation_list = self.load_images()
        self.char = pygame.image.load('zeus_right.png')
        self.direction = True

    def load_images(self):
        spritesheet = pygame.image.load('warrior.png')
        size = 162
        animation_steps = [10,8,1,7,7,3,7]
        data = [size]
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = spritesheet.subsurface(x*size, y*size, size, size)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)

    def attack(self, surface,  target, type):
        self.attacking = True
        if type == 1:  # ability 1 long range
            attacking_rect = pygame.Rect(0, 750 - self.char.y/4 + 10,
                                         1300, self.char.height/3)
            if attacking_rect.colliderect(target.char):
                target.health -= 2
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        elif type == 2:  # ability 2 medium range
            attacking_rect = pygame.Rect(self.char.centerx - (3.5 * self.char.width * self.flip), self.char.y,
                                         3.5 * self.char.width, self.char.height)
            if attacking_rect.colliderect(target.char):
                target.health -= 2
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        elif type == 3: # ultimate (need to change)
            attacking_rect = pygame.Rect(0, 750 - self.char.y/4 + 10,
                                         1300, self.char.height/3)
            if attacking_rect.colliderect(target.char):
                target.health -= 2
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)










