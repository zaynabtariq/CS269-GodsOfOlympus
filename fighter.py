"""
Gods of Olympus
Last Modified: 1/6/23
Course: CS269
File: fighter.py
"""

import pygame



class Fighter():
    def __init__(self, player, x, y, ledges):
        self.flip = False  # used to make sure the character is always facing the opponent
        self.player = player
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
        self.health = 100
        self.direction = True
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0

    
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
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.jump = True
                    self.vel_y = -30

                # attack
                if key[pygame.K_c] or key[pygame.K_v] or key[pygame.K_q]:
                    self.attacking = True
                    if key[pygame.K_c]:
                        self.attack_type = 1
                        self.attack(surface, target, self.attack_type)
                    if key[pygame.K_v]:
                        self.attack_type = 2
                        self.attack(surface, target, self.attack_type)
                    if key[pygame.K_q]:
                        self.attack_type = 3
                        self.attack(surface,target, self.attack_type)



            #check player 2 controls
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True

                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.jump = True
                    self.vel_y = -30

                # attack
                if key[pygame.K_PERIOD] or key[pygame.K_SLASH] or key[pygame.K_COMMA]:
                    self.attacking = True
                    if key[pygame.K_PERIOD]:
                        self.attack_type = 1
                        self.attack(surface, target, self.attack_type)
                    if key[pygame.K_SLASH]:
                        self.attack_type = 2
                        self.attack(surface,target, self.attack_type)
                    if key[pygame.K_COMMA]:
                        self.attack_type = 3
                        self.attack(surface, target, self.attack_type)

            # apply gravity
            if self.char.y < HEIGHT - 50:
                self.vel_y += GRAVITY
                dy += self.vel_y

            # ensures the player stays on screen
            if self.char.left + dx < 0:
                dx = -self.char.left
            if self.char.right + dx > WIDTH:
                dx = WIDTH - self.char.right
            if self.char.bottom + dy > HEIGHT - 100:  # write - X if there is a floor
                self.vel_y = 0
                self.jump = False
                dy = HEIGHT - self.char.bottom - 100 # write - X if there is a floor

            # ensures players are facing each other

            if target.char.centerx > self.char.centerx:
                self.flip = False
            else:
                self.flip = True

            #collision with ledges
            for ledge in ledges:
                if self.char.x >= ledge[0] and self.char.x <= (ledge[0] + ledge[2]):
                    if self.char.bottom <= ledge[1]:
                        self.vel_y = 0
                        #self.jump = False
                        dy = HEIGHT - self.char.bottom + ledge[1] - HEIGHT
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
            if attacking_rect.colliderect(target.char):
                target.health -= 2
                if self.flip == False:
                    target.char.x += 5
                else:
                    target.char.x -= 5
                # add a timer and make attacking false after 2 secs
            self.attacking = False






    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.char)



    
