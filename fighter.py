"""
Gods of Olympus
Last Modified: 1/20/23
Course: CS269
File: fighter.py
"""

import pygame
import random



class Fighter():
    def __init__(self, player, x, y, ledges, surface):
        self.attack_timer = 0
        self.flash_time = 0
        self.ultimate_time = 0
        self.attack_clock = pygame.time.Clock()
        self.ultimateAnimation = pygame.time.get_ticks()
        self.flip = False  # used to make sure the character is always facing the opponent
        self.player = player
        self.surface = surface
        self.name = None
        self.x = x
        self.y = y
        self.char = pygame.Rect((x, y, 50, 100))
        self.vel_y = 0
        self.jump = False
        self.running = False
        self.attack_type = 0
        self.attacking = False
        self.hit = False
        self.alive = True
        self.ultimate = False
        self.health = 100
        self.direction = True
        self.update_time = pygame.time.get_ticks()
        self.startUltimate = pygame.time.get_ticks() # start time for ultimate
        self.frame_index = 0
        # 0: idle right , 1: idle left , 2: left walk, 3: right walk, 4: ability1 left, 5: ability1 right,
        # 6: ability2 left, 7: ability2 right, 8: knock back right, 9: knock back left, 10: melee right, 11: melee left
        self.action = 0
        self.cooldown_time = 100 # cannot attack again within 0.1 seconds


    def move(self, WIDTH, HEIGHT, target, surface, ledges):
        SPEED = 10
        GRAVITY = 1.5
        dx = 0
        dy = 0
        #get keypresses
        key = pygame.key.get_pressed()

        #movement
        if self.attacking == False and self.alive == True:

            #check player 1 controls
            if self.player == 1:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                    self.action = 2

                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                    self.action = 3
                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.jump = True
                    self.vel_y = -30

                # attack
                if key[pygame.K_c] or key[pygame.K_v] or key[pygame.K_b] or key[pygame.K_q]:
                    if self.attack_clock.tick() > self.cooldown_time:
                        self.attacking = True
                        if key[pygame.K_v]:
                            self.attack_type = 1
                            self.action = 4
                            self.frame_index = 0
                            self.update_time = pygame.time.get_ticks()
                            self.attack_timer = pygame.time.get_ticks()
                            self.attack(surface, target, self.attack_type)
                        if key[pygame.K_b]:
                            self.attack_type = 2
                            self.action = 6
                            self.frame_index = 0
                            self.attack_timer = pygame.time.get_ticks()
                            self.update_time = pygame.time.get_ticks()
                            self.attack(surface, target, self.attack_type)
                        if key[pygame.K_c]:
                            self.action = 10
                            self.frame_index = 0
                            self.update_time = pygame.time.get_ticks()
                            self.attack_type = 3
                            self.attack(surface,target, self.attack_type)
                        if key[pygame.K_q]:
                            self.update_time = pygame.time.get_ticks()
                            self.startUltimate = pygame.time.get_ticks()
                            self.ultimateAnimation = pygame.time.get_ticks()
                            self.ultimate_time = pygame.time.get_ticks()
                            self.flash_time = pygame.time.get_ticks()
                            self.ultimate = True
                            self.attack_type = 4
                            self.attack(surface, target, self.attack_type)

            #check player 2 controls

            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                    self.action = 2
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
                    self.action = 3

                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.jump = True
                    self.vel_y = -30

                # attack
                if key[pygame.K_PERIOD] or key[pygame.K_SLASH] or key[pygame.K_COMMA] or key[pygame.K_m] :
                    if self.attack_clock.tick() > self.cooldown_time:
                        self.attacking = True
                        if key[pygame.K_PERIOD]:
                            self.update_time = pygame.time.get_ticks()
                            self.attack_type = 1
                            self.action = 5
                            self.frame_index = 0
                            self.update_time = pygame.time.get_ticks()
                            self.attack_timer = pygame.time.get_ticks()
                            self.attack(surface, target, self.attack_type)
                        if key[pygame.K_COMMA]:
                            self.attack_type = 2
                            self.action = 7
                            self.frame_index = 0
                            self.attack_timer = pygame.time.get_ticks()
                            self.update_time = pygame.time.get_ticks()
                            self.attack(surface,target, self.attack_type)
                        if key[pygame.K_SLASH]:
                            self.attack_type = 3
                            self.action = 11
                            self.frame_index = 0
                            self.update_time = pygame.time.get_ticks()
                            self.attack(surface, target, self.attack_type)
                        if key[pygame.K_m]:
                            self.update_time = pygame.time.get_ticks()
                            self.startUltimate = pygame.time.get_ticks()
                            self.ultimateAnimation = pygame.time.get_ticks()
                            self.ultimate_time = pygame.time.get_ticks()
                            self.flash_time = pygame.time.get_ticks()
                            self.ultimate = True
                            self.attack_type = 4
                            self.attack(surface, target, self.attack_type)

            # apply gravity
            if self.char.y < HEIGHT - 50:
                self.vel_y += GRAVITY
                dy += self.vel_y

            # Zeus passive
            if self.name == "Zeus" and self.jump == True:
                if self.player == 1:
                    if key[pygame.K_s]:
                        dy /= 7     # slows Zeus down
                elif self.player == 2:
                    if key[pygame.K_DOWN]:
                        dy /= 7     # slows Zeus down

            # ensures the player stays on screen
            if self.char.centerx + dx < 0:
                dx = -self.char.centerx
            if self.char.centerx + dx > WIDTH:
                dx = WIDTH - self.char.centerx
            if self.char.bottom + dy > HEIGHT - 100:  # write - X if there is a floor
                self.vel_y = 0
                self.jump = False
                dy = HEIGHT - self.char.bottom - 100 # write - X if there is a floor

            # ensures players are facing each other
            if target.char.centerx > self.char.centerx:
                self.flip = False
                if self.player == 2:
                    if self.action == 1:
                        self.action = 0
                    if self.action == 5:
                        self.action = 4
                    if self.action == 7:
                        self.action = 6
                    if self.action == 9:
                        self.action = 8
                    if self.action == 11:
                        self.action = 10

            else:
                self.flip = True
                if self.player == 1:
                    if self.action == 0:
                        self.action = 1
                    if self.action == 4:
                        self.action = 5
                    if self.action == 6:
                        self.action = 7
                    if self.action == 8:
                        self.action = 9
                    if self.action == 10:
                        self.action = 11

            # collision with ledges
            for ledge in ledges:
                if self.char.x >= ledge[0] - 190 and self.char.x <= (ledge[0] + ledge[2]) - 190:
                    if (self.char.colliderect(ledge) == True) and self.char.bottom <= ledge[1] + ledge[3]:
                        self.vel_y = 0
                        self.jump = False
                        if key[pygame.K_w] or key[pygame.K_UP]:
                            continue
                        else:
                            dy = - self.char.bottom + ledge[1]
                        if self.player == 1:
                            if key[pygame.K_s]:
                                self.vel_y = 30
                                dy = HEIGHT - self.char.bottom - 100
                        elif self.player == 2:
                            if key[pygame.K_DOWN]:
                                self.vel_y = 30
                                dy = HEIGHT - self.char.bottom - 100

            # update player position
            self.char.x += dx
            self.char.y += dy

    #General attack function
    def attack(self, surface,  target, type):
        self.attacking = True
        if type == 1:
            attacking_rect = pygame.Rect(self.char.centerx - (3.5 * self.char.width * self.flip), self.char.y,
                                         3.5 * self.char.width, self.char.height)
            if attacking_rect.colliderect(target.char.centerx):
                target.health -= 2
                if self.flip == False:
                    target.char.x += 5
                else:
                    target.char.x -= 5
                # add a timer and make attacking false after 2 secs
            self.attacking = False

    def random_melee(self):
        attack_damage = random.randint(1, 3)
        return attack_damage

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.char)
