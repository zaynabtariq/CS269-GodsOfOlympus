"""
Gods of Olympus
Last Modified: 1/23/23
Course: CS269
File: Poseidon.py
"""
import pygame
from fighter import Fighter

class Poseidon(Fighter):
    def __init__(self, player, x, y, ledges, surface):
        super().__init__(player, x, y, ledges, surface)
        self.wave_bottom = None
        self.waves = []
        self.num_waves = 0
        self.clock = pygame.time.Clock()
        self.x = x
        self.y = y
        self.animation_list = []
        self.attack_timer = None
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.ultimate_time = 0
        self.bubble = None
        self.name = 'Poseidon'
        # declaring flood variables
        self.flood_image = pygame.image.load('Images/flood_ability.png').convert_alpha()
        self.flood_image = pygame.transform.scale(self.flood_image, (1300, 300))
        # initial flood height
        self.flood_height = 700
        # load images
        #  0 : idle right
        temp_list = []
        for i in range (1,3):
            img = pygame.image.load(f'Images/poseidon_idle_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        #  1 : idle left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/poseidon_idle_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() *1.5, img.get_height() *1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 2 : walking left
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/poseidon_walkright_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 3 : walking right
        temp_list = []
        for i in range(1, 3):
            img = pygame.image.load(f'Images/poseidon_walkright_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 4 : ability1 right
        temp_list = []
        for i in range(1, 5):
            img = pygame.image.load(f'Images/poseidon_bubble_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 5 : ability1 left
        temp_list = []
        for i in range(4):
            img = self.animation_list[4][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 6 : ability2 right
        temp_list = []
        for i in range(1, 5):
            img = pygame.image.load(f'Images/poseidon_bubble_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 7 : ability2 left
        temp_list = []
        for i in range(4):
            img = self.animation_list[6][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)

        self.animation_list.append(temp_list)

        # 8 : attacked right (poseidon knock backs need to be added)
        temp_list = []
        for i in range(1, 5):
            img = pygame.image.load(f'Images/poseidon_knocback_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)


        # 9: attacked left (poseidon knock backs need to be added)
        temp_list = []
        for i in range(4):
            img = self.animation_list[8][i]
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)

        # 10: melee right
        temp_list = []
        for i in range(1,6):
            img = pygame.image.load(f'Images/poseidon_melee_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # 11: melee left
        temp_list = []
        for i in range(1,6):
            img = pygame.image.load(f'Images/poseidon_melee_{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            img_flipped = pygame.transform.flip(img, True, False)
            temp_list.append(img_flipped)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.char = self.image.get_rect()
        self.char.x = x
        self.char.y = y
        self.last_attack_time = 0

    def update(self, target):
        animation_cooldown = 0
        if self.action == 0 or self.action == 1:
            animation_cooldown = 270
        elif self.action == 2 or self.action == 3:
            animation_cooldown = 300
        elif self.action == 4 or self.action == 5:
            animation_cooldown = 300
            #bubble animation
            if self.bubble and pygame.time.get_ticks() - self.attack_timer < 2000:
                    self.bubble.radius += 5
                    if self.bubble.radius >= 165:
                        self.bubble.radius = 160
                    self.bubble.rect.center = self.char.center
                    self.bubble.image = pygame.transform.scale(self.bubble.image, (int(self.bubble.radius*2), int(self.bubble.radius*2)))
        elif self.action == 6 or self.action == 7:
            # ability 2 long range (wave) animation
            animation_cooldown = 300
            target_rect = (target.char.centerx - 50, target.char.y, 10, 220)
            for wave in self.waves:
                # pygame.draw.rect(surface, (0, 255, 0), target_rect)
                if wave.rect.colliderect(target_rect):
                    target.health -= 5 * self.damage_multiplier
                    self.waves.remove(wave)
                wave.update()

        elif self.action == 8 or self.action == 9:
            animation_cooldown = 100
        elif self.action == 10 or self.action == 11:
            animation_cooldown = 60

        # handle animation
        # update image
        try: # using try/except to fix the index out of range error
            self.image = self.animation_list[self.action][self.frame_index]
            # ultimate animation
            if self.ultimate:
                if self.flood_height > 530:
                    current_time = pygame.time.get_ticks()
                    if current_time - self.startUltimate >= 30:
                        self.flood_height -= 1.5
                        attacking_rect = self.flood_image.get_rect()
                        attacking_rect.x = 0
                        attacking_rect.y = self.flood_height
                        self.startUltimate = current_time
                        if attacking_rect.colliderect(target.char):
                            target.health -= 0.3 * self.damage_multiplier

                if pygame.time.get_ticks() - self.attack_timer > 6000:
                    self.ultimate = False
                    self.flood_height = 700



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
        surface.blit(self.image, self.char)
        if self.action == 4 or self.action == 5:
            # bubble
            if self.bubble and self.update_time - self.last_attack_time > 1500:
                surface.blit(self.bubble.image, self.bubble.pos)

        # wave ability
        if self.action == 6 or self.action == 7:
            for wave in self.waves:
                surface.blit(wave.wave_bottom, (0, 640))
                surface.blit(wave.image, wave.pos)
                if wave.pos[0] > 1300 or wave.pos[0] < 0:
                    self.waves.remove(wave)
                    self.num_waves -= 1

        # ultimate
        if self.ultimate:
            surface.blit(self.flood_image, (0, self.flood_height))


    def attack(self, surface,  target, type):
        self.attacking = True

        if type == 1:  # ability 1 medium range
            #attacking rectangle for bubble ability
            if self.update_time - self.last_attack_time > 1400:
                self.bubble = Bubble((self.char.centerx - 150, self.char.centery - 150), 100)
                self.attack_timer = pygame.time.get_ticks()
                ability1 = pygame.mixer.Sound('Game_sounds/Poseidon/poseidon_ability1.wav')
                ability1.play()
                attacking_rect = self.bubble.rect
                center = (target.char.centerx, target.char.centery)

                if attacking_rect.collidepoint(center):
                    target.health -= 6 * self.damage_multiplier
                    if not self.flip:
                        target.action = 9
                    else:
                        target.action = 8



        elif type == 2:  # ability 2 long range
            # making wave object
            if self.update_time - self.last_attack_time > 1500:
                self.last_attack_time = self.update_time
                ability2 = pygame.mixer.Sound('Game_sounds/Poseidon/wave.wav')
                ability2.play(0, 1000, 15)
                if target.char.centerx > self.char.centerx:
                    wave = Wave((self.char.centerx - (30 * self.flip), 540), (1, 0), 20)
                    self.wave_bottom = wave.wave_bottom
                    self.waves.append(wave)
                elif target.char.centerx < self.char.centerx:
                    wave = Wave((self.char.centerx - (30 * self.flip), 540), (-1, 0), 20)
                    self.wave_bottom = wave.wave_bottom
                    self.waves.append(wave)

                self.num_waves += 1


            # pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

        elif type == 3: # melee
            attacking_rect = pygame.Rect(self.char.centerx - (1/4 * self.char.width * self.flip), self.char.y,
                                         1 / 4 * self.char.width, self.char.height)
            #pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
            center = (target.char.centerx, target.char.centery)
            melee = pygame.mixer.Sound('Game_sounds/Poseidon/Metallic_hit.wav')
            melee.play()
            if attacking_rect.collidepoint(center):
                # does damage ranging from 1 to 3
                target.health -= Fighter.random_melee(self) * self.damage_multiplier
                if not self.flip:
                    target.char.x += 5
                    target.action = 9
                else:
                    target.char.x -= 5
                    target.action = 8

        elif type == 4:
            # starts the timer for ultimate
            self.attack_timer = pygame.time.get_ticks()
            ultimate = pygame.mixer.Sound('Game_sounds/Poseidon/Bubbly_sound.wav')
            ultimate.play(3)

        self.attacking = False

class Bubble:
    def __init__(self, character_pos, radius):
        self.pos = list(character_pos)
        self.radius = radius
        self.image = pygame.image.load("Images/bubble_attack.png")
        self.image = pygame.transform.scale(self.image, (int(self.radius * 2), int(self.radius * 2)))
        self.rect = pygame.Rect(character_pos[0] - 10 ,character_pos[1],int(self.radius * 2) + 60, int(self.radius * 2) + 50)

class Wave:
    def __init__(self, player_pos, wave_direction, speed):
        self.pos = list(player_pos)
        self.speed = speed
        self.direction = wave_direction
        self.wave_bottom = pygame.image.load('Images/wave_bottom.png')
        self.wave_bottom = pygame.transform.scale(self.wave_bottom, (1300, 120))
        if self.direction == (1, 0):
            self.image = pygame.image.load("Images/wave_top.png")
            self.image = pygame.transform.scale(self.image, (160, 120))
        elif self.direction == (-1, 0):
            self.image = pygame.image.load("Images/wave_top.png")
            self.image = pygame.transform.scale(self.image, (160, 120))
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()

    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        self.rect.center = self.pos
