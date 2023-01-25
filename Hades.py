"""
Gods of Olympus
Last Modified: 1/20/23
Course: CS269
File: Hades.py
"""
import pygame
from pygame import mixer
from fighter import Fighter

class Hades(Fighter):
    def __init__(self, player, x, y, ledges, surface):
        super().__init__(player, x, y, ledges, surface)
        self.x = x
        self.y = y
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.ultimate_time = 0
        self.flash_time = 0
        self.num_fireballs = 0
        self.name = 'Hades'
        # load images
        #  0 : idle right
        temp_list = []
        for i in range (1,3):
            img = pygame.image.load(f'Images/hades_idle_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() *1.5, img.get_height() *1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        #  1 : idle left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/hades_idle_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 2 : walking left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/hades_walkright_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 3 : walking right
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/hades_walkright_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 4 : ability1 right
        temp_list = []
        for i in range(1, 10):
            img = pygame.image.load(f'Images/hades_ability1_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 5 : ability1 left
        temp_list = []
        for i in range(9):
            img = self.animation_list[4][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 6 : ability2 right
        temp_list = []
        for i in range(1, 6):
            img = pygame.image.load(f'Images/hades_ability2_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 7 : ability2 left
        temp_list = []
        for i in range(5):
            img = self.animation_list[6][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)

        self.animation_list.append(temp_list)

        # 8 : attacked right
        temp_list = []
        for i in range(1, 5):
            img = pygame.image.load(f'Images/hades_knockback_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)


        # 9: attacked left
        temp_list = []
        for i in range(4):
            img = self.animation_list[8][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 10: melee right
        temp_list = []
        for i in range(1,7):
            img = pygame.image.load(f'Images/hades_melee_{i}.png')
            img_flipped = pygame.transform.flip(img, True, False)
            img_flipped = pygame.transform.scale(img_flipped, (img_flipped.get_width() * 1.5, img_flipped.get_height() * 1.5))
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 11: melee left
        temp_list = []
        for i in range(1,7):
            img = pygame.image.load(f'Images/hades_melee_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.char = self.image.get_rect()
        self.char.x = x
        self.char.y = y
        self.direction = True
        self.fireballs = []
        self.last_attack_time = 0

    def update(self, target):
        animation_cooldown = 0
        if self.action == 0 or self.action == 1:
            animation_cooldown = 270
        elif self.action == 2 or self.action == 3:
            animation_cooldown = 300
        elif self.action == 4 or self.action == 5:
            animation_cooldown = 100
        elif self.action == 6 or self.action == 7:
            animation_cooldown = 150
            target_rect = (target.char.centerx - 10, target.char.y, 20, 220)
            for fireball in self.fireballs:
                fireball.update()
                # pygame.draw.rect(surface, (0, 255, 0), target_rect)
                if fireball.rect.colliderect(target_rect):
                    target.health -= 2
                    self.fireballs.remove(fireball)

        elif self.action == 8 or self.action == 9:
            animation_cooldown = 100
        elif self.action == 10 or self.action == 11:
            animation_cooldown = 60


        # handle animation
        # update image
        try: # using try/except to fix the index out of range error
            self.image = self.animation_list[self.action][self.frame_index]
        except:
            print("Try/Except")

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
        if not self.ultimate:
            surface.blit(self.image, self.char)
        if self.ultimate:
            current_time = pygame.time.get_ticks()
            if current_time - self.ultimate_time > 9000:
                self.ultimate = False
                self.ultimate_time = 0
            elif current_time - self.flash_time > 3000:
                # Flash the player here
                surface.blit(self.image, self.char)
                # reset flash time
                self.flash_time = current_time

        if self.action == 6 or self.action == 7:
            for fireball in self.fireballs:
                surface.blit(fireball.image, fireball.pos)
                if fireball.pos[0] > 1300 or fireball.pos[0] < 0 or fireball.pos[1] > 750 or fireball.pos[1] < 0:
                    self.fireballs.remove(fireball)
                    self.num_fireballs -= 1

    def attack(self, surface,  target, type):
        self.attacking = True

        if type == 1:  # ability 1 medium range
            attacking_rect = pygame.Rect(self.char.centerx - (1 / 2 * self.char.width * self.flip), self.char.y,
                                         1 / 2 * self.char.width, self.char.height)
            center = (target.char.centerx, target.char.centery)
            # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

            if attacking_rect.collidepoint(center):
                target.health -= 5

                if self.health < 100:
                    self.health += 3

                if not self.flip:
                    target.char.x += 70
                    target.action = 9
                else:
                    target.char.x -= 70
                    target.action = 8


        elif type == 2:  # ability 2 long range

            if self.update_time - self.last_attack_time > 1500:
                # create fireball in 3 directions
                self.last_attack_time = self.update_time
                fireball = Fireball((self.char.centerx - (50 * self.flip), self.char.centery), (0, -1), 20)
                self.fireballs.append(fireball)
                fireball = Fireball((self.char.centerx - (50 * self.flip), self.char.centery), (1, 0), 20)
                self.fireballs.append(fireball)
                fireball = Fireball((self.char.centerx - (50 * self.flip), self.char.centery), (-1, 0), 20)
                self.fireballs.append(fireball)
                self.num_fireballs += 1
                fireball = pygame.mixer.Sound('Game_sounds/Hades/Fireball.wav')
                fireball.play()

            # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        elif type == 3: # melee
            attacking_rect = pygame.Rect(self.char.centerx - (1 / 4 * self.char.width * self.flip), self.char.y,
                                         1 / 4 * self.char.width, self.char.height)
            melee = pygame.mixer.Sound('Game_sounds/Hades/Melee.wav')
            melee.play()
            #pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            center = (target.char.centerx, target.char.centery)
            if attacking_rect.collidepoint(center):
                # does damage ranging from 1 to 3
                target.health -= Fighter.random_melee(self)
                if not self.flip:
                    target.char.x += 5
                    target.action = 9
                else:
                    target.char.x -= 5
                    target.action = 8

        self.attacking = False

class Fireball:
    def __init__(self, player_pos, fireball_direction, speed):
        self.pos = list(player_pos)
        self.speed = speed
        self.direction = fireball_direction
        if self.direction == (1, 0):
            self.image = pygame.image.load("Images/hades_fireball.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.direction == (-1, 0):
            self.image = pygame.image.load("Images/hades_fireball.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = pygame.image.load("Images/hades_fireball.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()


    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        self.rect.center = self.pos
