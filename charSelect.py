"""
Gods of Olympus
Last Modified: 1/24/23
Course: CS269
File: titleScreen.py
"""

import pygame
import pygame_gui
from pygame.locals import *

class charSelect():

    # Constructor
    def __init__(self, x, y, window_surface, char_image_size):
        self.x = x
        self.y = y
        self.window_surface = window_surface
        self.char_image_size = char_image_size

        self.p1_character = "Zeus"
        self.p2_character = "Hades"
        self.map = "null"
        self.button_theme = "sky_theme.json"

        self.background = pygame.Surface((self.x, self.y))
        self.bg_and_characters = pygame.Surface((self.x, self.y))

        # Button arrays
        self.all_buttons = []
        self.all_managers = []   # Holds button managers

    # Colors all visible pixels of an image
    def color_surface(self, surface, red, green, blue):
        arr = pygame.surfarray.pixels3d(surface)
        arr[:,:,0] = red
        arr[:,:,1] = green
        arr[:,:,2] = blue

    # Adds maps
    def add_maps(self):

        map_size_x = 550
        map_size_y = 350
        map_file = ""
        map_bg = pygame.Rect(-3 + (self.x - map_size_x) / 2, -3 + 20, map_size_x + 6, map_size_y + 6)
        map_bg_color = (255, 255, 255)

        # Making add_maps adjustable when clicked
        if self.map == "Zeus":
            map_file = "Images/sky_palace.jpg"
        elif self.map == "Hades":
            map_file = "Images/hades_palace.jpg"
        elif self.map == "Poseidon":
            map_file = "Images/water_palace.jpg"
        else:   # If Character Select screen is called for the first time
            self.map = "Zeus"
            map_file = "Images/sky_palace.jpg"

            # Create map_image
            map_image = pygame.image.load(map_file).convert_alpha()
            map_image = pygame.transform.scale(map_image, (map_size_x, map_size_y))

            # Add map_image
            self.background.blit(map_image, ((self.x - map_size_x) / 2, 20))

        # Add map_bg & map_image
        map_image = pygame.image.load(map_file).convert_alpha()
        map_image = pygame.transform.scale(map_image, (map_size_x, map_size_y))
        pygame.draw.rect(self.background, map_bg_color, map_bg)
        self.background.blit(map_image, ((self.x - map_size_x) / 2, 20))
        self.bg_and_characters.blit(map_image, ((self.x - map_size_x) / 2, 20))

    # Adds characters
    def add_characters(self):

        # Adds bubble around characters
        def add_bubbles():
            platform_size_x = 350
            platform_size_y = 400

            platform_1 = pygame.image.load("Images/bubble.png").convert_alpha()
            platform_1 = pygame.transform.scale(platform_1, (platform_size_x, platform_size_y))

            platform_2 = pygame.image.load("Images/bubble.png").convert_alpha()
            platform_2 = pygame.transform.scale(platform_2, (platform_size_x, platform_size_y))
            #self.color_surface(platform_2, 255, 0, 0)      # --> Image has unknown sRGB profile

            self.bg_and_characters.blit(platform_1, (0, platform_size_y - 95))
            self.bg_and_characters.blit(platform_1, (self.x - platform_size_x, platform_size_y - 95))

        # Sets character image
        def set_character(player):
            player_image = ""

            if player == "Zeus":
                player_image = pygame.image.load("Images/zeusmain.png").convert_alpha()
            elif player == "Hades":
                player_image = pygame.image.load("Images/hadesmain.png").convert_alpha()
            else:
                player_image = pygame.image.load("Images/poseidonmain.png").convert_alpha()

            player_image = pygame.transform.scale(player_image, (self.char_image_size, self.char_image_size))
            return player_image

        # Finds player image x location
        def find_character_locations():
            p1_location = 0
            p2_location = 0

            # Player 1
            if self.p1_character == "Zeus":
                p1_location = -55
            elif self.p1_character == "Hades":
                p1_location = -70
            else:
                p1_location = -70   # May need to be adjusted

            # Player 2
            if self.p2_character == "Zeus":
                p2_location = self.x - self.char_image_size + 98
            elif self.p2_character == "Hades":
                p2_location = self.x - self.char_image_size + 80
            else:
                p2_location = self.x - self.char_image_size + 80    # May need to be adjusted

            return p1_location, p2_location

        # Clears surface
        self.bg_and_characters.blit(self.background, (0, 0))

        # Adds character images
        p1_image = set_character(self.p1_character)
        p2_image = set_character(self.p2_character)

        # Add character in at proper location
        add_bubbles()
        p1_location, p2_location = find_character_locations()
        self.bg_and_characters.blit(p1_image, (p1_location, self.y / 4 + 35))
        self.bg_and_characters.blit(p2_image, (p2_location, self.y / 4 + 35))

    # Method to make the arrow button
    def makeButton(self, manager, text, size_x, size_y, location_x, location_y):
        button = pygame_gui.elements.UIButton(pygame.Rect((location_x, location_y), (size_x, size_y)), text = text, manager = manager)
        return button

    # Initialize character select
    def initialize_char_select(self):

        # Set up background
        pygame.display.set_caption('Character Selection')
        sky_image = pygame.image.load("Images/sky2.png").convert_alpha()
        sky_image = pygame.transform.scale(sky_image, (self.x, self.y))
        cloud = pygame.image.load("Images/sky_floor.png").convert_alpha()
        self.background.blit(sky_image, (0, 0))
        self.background.blit(cloud, (0, self.y - 115))

        # Set music
        pygame.mixer.music.unload()
        pygame.mixer.music.load('Game_sounds/Player_select.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        self.add_maps()
        self.add_characters()

        # Make character buttons
        manager1 = pygame_gui.UIManager((self.x, self.y), self.button_theme)
        manager2 = pygame_gui.UIManager((self.x, self.y), self.button_theme)
        self.all_managers.append(manager1)
        self.all_managers.append(manager2)

        button_1 = self.makeButton(manager1, 'Player 1', 250, 70, 45, self.y - 125 + 33)
        button_2 = self.makeButton(manager2, 'Player 2', 250, 70, self.x - 250 - 45, self.y - 125 + 33)
        self.all_buttons.append(button_1)
        self.all_buttons.append(button_2)

        # Make map button
        manager3 = pygame_gui.UIManager((self.x, self.y), self.button_theme)
        self.all_managers.append(manager3)
        button_3 = self.makeButton(manager3, 'Map', 350, 70, (self.x / 2) - 175, (self.y / 2) - 3)
        self.all_buttons.append(button_3)

        # BUG: Buttons don't appear without mouse movement first???

        self.window_surface.blit(self.background, (0, 0))

    # Run character selection screen
    def loop_for_characters(self):
        p1_character_num = 1
        p2_character_num = 2
        map_num = 1

        clock = pygame.time.Clock()

        # Loop
        while True:
            time_delta = clock.tick(60)/1000.0

            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if key[pygame.K_ESCAPE] or event.type == QUIT:  # If user quits selection screen

                    # Set player 1 character
                    if self.p1_character == "Zeus":
                        p1_character_num = 1
                    elif self.p1_character == "Hades":
                        p1_character_num = 2
                    else:
                        p1_character_num = 3

                    # Set player 2 character
                    if self.p2_character == "Zeus":
                        p2_character_num = 1
                    elif self.p2_character == "Hades":
                        p2_character_num = 2
                    else:
                        p2_character_num = 3

                    # Set map
                    if self.map == "Zeus":
                        map_num = 1
                    elif self.map == "Hades":
                        map_num = 2
                    else:
                        map_num = 3

                    print('Characters selected:', p1_character_num, ',', p2_character_num, '| Map selected:', map_num)
                    return p1_character_num, p2_character_num, map_num   # Returns number for characters & maps selected

                if event.type == pygame_gui.UI_BUTTON_PRESSED:  # If a button is pressed
                    if event.ui_element == self.all_buttons[0]: # P1 button
                        #print('Button_1 pressed')
                        if self.p1_character == "Zeus":
                            self.p1_character = "Hades"
                        elif self.p1_character == "Hades":
                            self.p1_character = "Poseidon"
                        else:
                            self.p1_character = "Zeus"
                        self.add_characters()
                    if event.ui_element == self.all_buttons[1]: # P2 button
                        #print('Button_2 pressed')
                        if self.p2_character == "Zeus":
                            self.p2_character = "Hades"
                        elif self.p2_character == "Hades":
                            self.p2_character = "Poseidon"
                        else:
                            self.p2_character = "Zeus"
                        self.add_characters()
                    if event.ui_element == self.all_buttons[2]: # Map button
                        #print('Button_3 pressed')
                        if self.map == "Zeus":
                            self.map = "Hades"
                            self.add_maps()
                        elif self.map == "Hades":
                            self.map = "Poseidon"
                            self.add_maps()
                        else:
                            self.map = "Zeus"
                            self.add_maps()

                # Update events (button hovering or clicking)
                for manager in self.all_managers:
                    manager.process_events(event)
                    manager.update(time_delta)

            self.window_surface.blit(self.bg_and_characters, (0, 0))

            # Draw buttons
            for manager in self.all_managers:
                manager.draw_ui(self.window_surface)

            pygame.display.update()
