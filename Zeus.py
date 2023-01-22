"""
Gods of Olympus
Last Modified: 1/21/23
Course: CS269
File: Zeus.py
"""
import pygame
from fighter import Fighter

class Zeus(Fighter):
    def __init__(self, player, x, y, ledges, surface):
        super().__init__(player, x, y, ledges, surface)
        self.lightning = pygame.image.load('Images/lightning7.png')
        self.x = x
        self.y = y
        self.animation_list = []
        self.frame_index = 0
        self.index = 0
        self.update_time = pygame.time.get_ticks()
        #load images
        #  0 : idle right
        temp_list = []
        for i in range (1,3):
            img = pygame.image.load(f'Images/idle_redo_right_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() *1.5, img.get_height() *1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #  1 : idle left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/idle_redo_left_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 2 : walking left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/leftwalk_redo_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)


        # 3 : walking right
        temp_list = []
        for i in range(2):
            img = self.animation_list[2][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 4 : ability1
        temp_list = []
        for i in range(1, 6):
            img = pygame.image.load(f'Images/ability1_redo_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 5 : ability1 left

        temp_list = []
        for i in range(2, 6):
            img = pygame.image.load(f'Images/left_ability1_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 6 : ability2
        temp_list = []
        for i in range(1, 12):
            img = pygame.image.load(f'Images/right_ability2_redo_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 7 : ability2 left
        temp_list = []
        for i in range(11):
            img = self.animation_list[6][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 8 : attacked right
        temp_list = []
        for i in range(1, 7):
            img = pygame.image.load(f'Images/knockback_redo_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 9: attacked left
        temp_list = []
        for i in range(6):
            img = self.animation_list[8][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 10: melee right
        temp_list = []
        for i in range(1, 6):
            img = pygame.image.load(f'Images/zeus_melee_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 11: melee left
        temp_list = []
        for i in range(5):
            img = self.animation_list[10][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # ultimate
        self.ultimateList = []
        for i in range(1, 5):
            img = pygame.image.load(f'Images/ultimate{i}.png')
            img = pygame.transform.scale(img, (200, 250))
            self.ultimateList.append(img)

        self.ultimate_img = self.ultimateList[self.index]
        self.image = self.animation_list[self.action][self.frame_index]
        self.char = self.image.get_rect()
        self.char.x = x
        self.char.y = y
        self.direction = True



    def update(self):
        animation_cooldown = 0
        if self.action == 0 or self.action == 1:
            animation_cooldown = 270
        elif self.action == 2 or self.action == 3:
            animation_cooldown = 300
        elif self.action == 4 or self.action == 5:
            animation_cooldown = 80
        elif self.action == 6 or self.action == 7:
            animation_cooldown = 80
        elif self.action == 8 or self.action == 9:
            animation_cooldown = 50
        elif self.action == 10 or self.action == 11:
            animation_cooldown = 60


        # handle animation
        # update image

        try:  # using the try/except to fix index out of range error
            self.image = self.animation_list[self.action][self.frame_index]
            # adds the animation for ultimate
            if self.ultimate:
                self.index = 0
                self.ultimate_img = self.ultimateList[self.index]
                if pygame.time.get_ticks() - self.ultimateAnimation > animation_cooldown:
                    self.ultimateAnimation = pygame.time.get_ticks()
                    self.index += 1
                if self.index >= len(self.ultimateList):
                    self.index = 0

            # adds lightning if ability 2 is used
            if self.action == 6 or self.action == 7:
                img = pygame.image.load(f'Images/lightning7.png')
                img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
                img = pygame.transform.scale(img, (1300, 70))
                self.lightning = img
        except:
            print("Try/Except")

        # check if enough time has been passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()
            if self.ultimate:
                if pygame.time.get_ticks() - self.startUltimate > 8000:
                    self.ultimate = False



    def idle(self):
        if self.player == 1:
            self.action = 0
        elif self.player == 2:
            self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        surface.blit(self.image, self.char)
        if self.ultimate:
            surface.blit(self.ultimate_img, (self.char.centerx - 100, self.char.y))
        if self.action == 6 or self.action == 7:
            surface.blit(self.lightning, (0, 600))

    def attack(self, surface,  target, type):
        self.attacking = True

        if type == 1:  # ability 1 medium range
            attacking_rect = pygame.Rect(self.char.centerx - (1/2 * self.char.width * self.flip), self.char.y,
                                         1/2 * self.char.width, self.char.height)
            center = (target.char.centerx, target.char.centery)
            # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

            if attacking_rect.collidepoint(center):
                if not self.ultimate:
                    target.health -= 2
                else:
                    target.health -= 4  # ultimate doubles the damage

        elif type == 2:  # ability 2 long range
            attacking_rect = pygame.Rect(0, 750 - self.char.y/3 + 10,
                                         1300, self.char.height/3)
            if attacking_rect.colliderect(target.char):
                if not self.ultimate:
                    target.health -= 2
                else:
                    target.health -= 4  # ultimate doubles the damage

                # knockback animation
                if not self.flip:
                    target.char.x += 100
                    target.action = 9
                else:
                    target.char.x -= 100
                    target.action = 8

            for i in range(1, 8):
                # loads lightening images
                img = pygame.image.load(f'Images/lightning{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
                attacking_rect_img = img
                attacking_rect_img_scaled = pygame.transform.scale(attacking_rect_img, (1300, 70))
                surface.blit(attacking_rect_img_scaled, (0, 600))
            # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        elif type == 3: # melee
            attacking_rect = pygame.Rect(self.char.centerx - (2.5 * self.char.width * self.flip), self.char.y,
                                         1 / 4 * self.char.width, self.char.height)
            # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            center = (target.char.centerx, target.char.centery)
            if attacking_rect.collidepoint(center):
                # does damage ranging from 1 to 3
                if not self.ultimate:
                    target.health -= Fighter.random_melee(self)
                else:
                    target.health -= 2*(Fighter.random_melee(self)) # ultimate doubles the damage
                # knockback animation
                if not self.flip:
                    target.char.x += 150
                    target.action = 9
                else:
                    target.char.x -= 150
                    target.action = 8

        self.attacking = False
