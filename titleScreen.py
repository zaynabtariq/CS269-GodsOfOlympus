"""
Gods of Olympus
Last Modified: 1/19/23
Course: CS269
File: titleScreen.py
"""

import pygame
import pygame_gui

class titleScreen():

    # Constructor
    def __init__(self, x, y, window_surface):
        self.x = x
        self.y = y
        self.window_surface = window_surface

    # Creates all main buttons
    def createAllButtons(self):

        # Method to make a standard button
        def makeStandardButton(location_y, the_text, the_manager):
            button = pygame_gui.elements.UIButton(pygame.Rect((location_x, location_y), (size_x, size_y)), text = the_text, manager = the_manager)
            return button

        # Method to make the settings button
        def makeSettingsButton(the_manager):
            settings_button = pygame_gui.elements.UIButton(pygame.Rect((settings_location_x, settings_location_y), (settings_size, settings_size)), text = '', manager = the_manager)
            return settings_button


        # Standard button variables
        size_x = 200
        size_y = 50
        location_x = (self.x / 2) - (size_x / 2)
        location_y = (self.y / 2) + (size_y / 2) + 55    # 55 is changeable pixel amount for the height of the buttons
        space_inbetween_buttons = size_y + (size_y / 2)
        border_size = 1

        # Settings button variables
        settings_size = 40
        distance_from_edge = 10
        settings_location_x = self.x - settings_size - distance_from_edge
        settings_location_y = distance_from_edge

        # Define button managers
        all_managers = []
        for i in range(0, 5):
            manager = pygame_gui.UIManager((self.x, self.y), 'sky_theme.json')   # Can remove sky_theme.json to remove button themes
            all_managers.append(manager)

        # Button 1 ('Play' button)
        button_1_y = location_y     # location_y of button_1
        button_1 = makeStandardButton(button_1_y, 'Play', all_managers[0])

        # Button 2 ('Character select' button)
        button_2_y = button_1_y + space_inbetween_buttons    # Adding size_y to account for first button size. Unnecessary for following buttons
        button_2 = makeStandardButton(button_2_y, 'Character Select', all_managers[1])

        # Button 3 ('Freeplay' button)
        button_3_y = button_2_y + space_inbetween_buttons
        button_3 = makeStandardButton(button_3_y, 'Freeplay', all_managers[2])

        # Button 4 ('Controls' button)
        button_4_y = button_3_y + space_inbetween_buttons
        button_4 = makeStandardButton(button_4_y, 'Controls', all_managers[3])

        # Button 5 ('Settings' button) -> unique location
        button_5 = makeSettingsButton(all_managers[4])

        all_buttons = [button_1, button_2, button_3, button_4, button_5]

        return all_buttons, all_managers

    # Colors all visible pixels of an image
    def color_surface(self, surface, red, green, blue):
        arr = pygame.surfarray.pixels3d(surface)
        arr[:,:,0] = red
        arr[:,:,1] = green
        arr[:,:,2] = blue

    # Initializes the title screen
    def initializeTitleScreen(self):
        pygame.display.set_caption('Title Screen')

        background = pygame.Surface((self.x, self.y))
        sky_image = pygame.image.load("Images/sky.png").convert_alpha()
        background.blit(sky_image, (0, 0))

        # Add the background to the surface
        self.window_surface.blit(background, (0, 0))
        cloud = pygame.image.load("Images/sky_floor.png").convert_alpha()
        background.blit(cloud, (0, self.y - 115))

        # Add characters to screen
        fighter_image_size = 500

        fighter_1_image = pygame.image.load("Images/zeusmain.png").convert_alpha()
        fighter_1_art = pygame.transform.scale(fighter_1_image, (fighter_image_size, fighter_image_size))
        fighter_2_image = pygame.image.load("Images/hadesmain.png").convert_alpha()
        #fighter_2_image = pygame.transform.flip(fighter_2_image, True, False)   # Flip surface horizontally
        fighter_2_art = pygame.transform.scale(fighter_2_image, (fighter_image_size, fighter_image_size))

        background.blit(fighter_1_art, (-100, self.y / 5 + 70))     # Adding 70 to land on cloud, can be removed if want to add platform
        background.blit(fighter_2_art, (self.x - fighter_image_size + 100, self.y / 5 + 70))

        # Add logo/text/image
        image_size_x = 700
        image_size_y = 400

        center_image = pygame.image.load("Images/Logo.png").convert_alpha()
        center_image = pygame.transform.scale(center_image, (image_size_x, image_size_y))
        background.blit(center_image, ((self.x - image_size_x) / 2, 0))

        # Update background
        self.window_surface.blit(background, (0, 0))