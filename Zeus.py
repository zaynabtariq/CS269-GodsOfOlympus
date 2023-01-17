"""
Gods of Olympus
Last Modified: 1/17/23
Course: CS269
File: zeus.py
"""
import pygame
from fighter import Fighter

class Zeus(Fighter):
    def __init__(self, player, x, y, ledges):
        super().__init__(player, x, y, ledges)
        self.x = x
        self.y = y
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        #load images
        #  0 : idle right
        temp_list = []
        for i in range (1,3):
            img = pygame.image.load(f'idle_right_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() *1.5, img.get_height() *1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #  1 : idle left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'idle_left_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 2 : walking left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'leftwalk_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)


        # 3 : walking right
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'rightwalk_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 4 : ability1
        temp_list = []
        for i in range(2, 6):
            img = pygame.image.load(f'ability1_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 5 : ability1 left
        temp_list = []
        for i in range(2, 6):
            img = pygame.image.load(f'left_ability1_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 6 : ability2
        temp_list = []
        for i in range(1, 12):
            img = pygame.image.load(f'right_ability2_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.char = self.image.get_rect()
        self.char.x = x
        self.char.y = y
        self.direction = True


    def update(self):
        if self.action == 0 or self.action == 1:
            animation_cooldown = 270
        elif self.action == 2 or self.action == 3:
            animation_cooldown = 300
        elif self.action == 4 or self.action == 5:
            animation_cooldown = 80
        elif self.action == 6 or self.action == 7:
            animation_cooldown = 80

        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]


        # check if enough time has been passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()



    def idle(self):
        if self.player == 1:
            self.action = 0
        elif self.player == 2:
            self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        surface.blit(self.image, self.char)



    def attack(self, surface,  target, type):
        self.attacking = True

        if type == 1:  # ability 1 medium range
            attacking_rect = pygame.Rect(self.char.centerx - (2 * self.char.width * self.flip), self.char.y,
                                         2 * self.char.width, self.char.height)
            if attacking_rect.colliderect(target.char):
                target.health -= 2

        elif type == 2:  # ability 2 long range
            attacking_rect = pygame.Rect(0, 750 - self.char.y/3 + 10,
                                         1300, self.char.height/3)
            if attacking_rect.colliderect(target.char):
                target.health -= 2


            for i in range(1, 8):
                img = pygame.image.load(f'lightning{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
                attacking_rect_img = img
                attacking_rect_img_scaled = pygame.transform.scale(attacking_rect_img, (1300, 60))
                surface.blit(attacking_rect_img_scaled, (0, 600))






            #pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        elif type == 3: # ultimate (need to change)
            attacking_rect = pygame.Rect(0, 750 - self.char.y/4 + 10,
                                         1300, self.char.height/3)
            if attacking_rect.colliderect(target.char):
                target.health -= 2
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        self.attacking = False









