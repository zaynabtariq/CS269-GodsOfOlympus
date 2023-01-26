"""
Gods of Olympus
Last Modified: 1/25/23
Course: CS269
File: helperUI.py
"""

import pygame
import pygame_gui

class helperUI():

    # Constructor
    def __init__(self, x, y, window_surface):
        self.x = x
        self.y = y
        self.window_surface = window_surface

    # Creates text at the given location
    def create_text(self, surface, text, font_size, location_x, location_y):
        color = (0, 201, 255)

        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(text, True, color)
        textRect = text.get_rect()
        
        # Set text position & blit text
        textRect.center = (location_x / 2, location_y / 2)
        surface.blit(text, textRect)

        return text

    # Brings up controls gui
    def initialize_control_gui(self):
        # GUI variables
        border_size = 3
        surface_extension = 70
        size_x = self.x / 2 - (border_size * 2) + (surface_extension * 2)
        size_y = self.y / 2 + 30 - (border_size * 2)

        # Set up control_gui screen
        contr_surface_bg = pygame.Surface((size_x + (border_size * 2), size_y + (border_size * 2)))
        contr_surface_bg.fill("#00c9ff")
        surface_bg_color = (0, 201, 255)

        contr_surface = pygame.Surface((size_x, size_y))
        contr_surface.fill("#6de1ff")
        #surface_color = (109, 225, 255)

        # Create lines
        line_width = 3
        vertical_line = pygame.Rect((size_x / 2 - (line_width / 2)), 60, line_width, size_y)    # Side, Top, Width, Height
        horizontal_line = pygame.Rect(0, 60, size_x, line_width)
        pygame.draw.rect(contr_surface, surface_bg_color, vertical_line)
        pygame.draw.rect(contr_surface, surface_bg_color, horizontal_line)

        underline_1 = pygame.Rect(100, 148, 192, line_width - 1)
        underline_2 = pygame.Rect(492, 148, 192, line_width - 1)
        underline_3 = pygame.Rect(123, 283, 147, line_width - 1)
        underline_4 = pygame.Rect(515, 283, 147, line_width - 1)
        pygame.draw.rect(contr_surface, surface_bg_color, underline_1)
        pygame.draw.rect(contr_surface, surface_bg_color, underline_2)
        pygame.draw.rect(contr_surface, surface_bg_color, underline_3)
        pygame.draw.rect(contr_surface, surface_bg_color, underline_4)

        # Create text
        self.create_text(contr_surface, 'Controls', 36, size_x, 65)
        self.create_text(contr_surface, 'Player 1', 30, 130, 170)
        self.create_text(contr_surface, 'Player 2', 30, size_x * 2 - 130, 170)

        self.create_text(contr_surface, 'Movement keys', 24, (size_x / 2), 270)   # Player 1 movement
        self.create_text(contr_surface, 'Up:', 24, 75, 350)
        self.create_text(contr_surface, 'Left:', 24, (size_x / 2) - 25, 350)
        self.create_text(contr_surface, 'Right:', 24, (size_x - 115), 350)
        self.create_text(contr_surface, 'W', 36, 75, 430)
        self.create_text(contr_surface, 'A', 36, (size_x / 2) - 25, 430)
        self.create_text(contr_surface, 'D', 36, (size_x - 115), 430)

        self.create_text(contr_surface, 'Movement keys', 24, size_x + (size_x / 2), 270)  # Player 2 movement
        self.create_text(contr_surface, 'Up:', 24, size_x + 75, 350)
        self.create_text(contr_surface, 'Left:', 24, size_x + (size_x / 2) - 25, 350)
        self.create_text(contr_surface, 'Right:', 24, size_x + (size_x - 115), 350)
        self.create_text(contr_surface, '^', 40, size_x + 75, 450)
        self.create_text(contr_surface, '<', 36, size_x + (size_x / 2) - 25, 430)
        self.create_text(contr_surface, '>', 36, size_x + (size_x - 115), 430)

        self.create_text(contr_surface, 'Ability keys', 24, (size_x / 2), 540)   # Player 1 ability
        self.create_text(contr_surface, 'Melee:', 24, 100, 620)
        self.create_text(contr_surface, 'A1:', 24, (size_x / 2) - 100, 620)
        self.create_text(contr_surface, 'A2:', 24, (size_x / 2) + 100, 620)
        self.create_text(contr_surface, 'Ult:', 24, (size_x / 2) + 300, 620)
        self.create_text(contr_surface, 'C', 36, 100, 700)
        self.create_text(contr_surface, 'V', 36, (size_x / 2) - 100, 700)
        self.create_text(contr_surface, 'B', 36, (size_x / 2) + 100, 700)
        self.create_text(contr_surface, 'Q', 36, (size_x / 2) + 300, 700)

        self.create_text(contr_surface, 'Ability keys', 24, size_x + (size_x / 2), 540)  # Player 2 ability
        self.create_text(contr_surface, 'Ult:', 24, size_x + 75, 620)
        self.create_text(contr_surface, 'A2:', 24, size_x + (size_x / 2) - 140, 620)
        self.create_text(contr_surface, 'A1:', 24, size_x + (size_x / 2) + 60, 620)
        self.create_text(contr_surface, 'Melee:', 24, size_x + (size_x / 2) + 260, 620)
        self.create_text(contr_surface, 'M', 36, size_x + 75, 700)
        self.create_text(contr_surface, ',', 36, size_x + (size_x / 2) - 140, 700)
        self.create_text(contr_surface, '.', 36, size_x + (size_x / 2) + 60, 700)
        self.create_text(contr_surface, '/', 36, size_x + (size_x / 2) + 260, 700)

        # Blit gui
        self.window_surface.blit(contr_surface_bg, (self.x / 4 - surface_extension, self.y / 32))
        self.window_surface.blit(contr_surface, (self.x / 4 + border_size - surface_extension, self.y / 32 + border_size))

    # Initializes setting gui
    def initialize_settings_gui(self, in_game, all_buttons, all_managers, all_text, all_text_rect):

        border_size = 3
        size_x = self.x / 3 - (border_size * 2)
        size_y = self.y / 3 - 60 - (border_size * 2)
        if in_game:
            all_buttons_min_length = 0  # Number of buttons in all_buttons NOT INCLUDING Resume & Exit of settings gui
        else:
            all_buttons_min_length = 5

        # Set up settings_gui screen
        sett_surface_bg = pygame.Surface((size_x + (border_size * 2), size_y + (border_size * 2)))
        sett_surface_bg.fill("#00c9ff")
        surface_bg_color = (0, 201, 255)

        sett_surface = pygame.Surface((size_x, size_y))
        sett_surface.fill("#6de1ff")

        # Add data
        underline = pygame.Rect(147, 38, 133, 2)
        pygame.draw.rect(sett_surface, surface_bg_color, underline)
        self.create_text(sett_surface, 'Settings', 30, size_x, 45)

        # Initializes buttons if needed
        if len(all_buttons) <= all_buttons_min_length:  # If list does not have resume & quit button
            resume_manager = pygame_gui.UIManager((self.x, self.y), 'sky_theme.json')
            resume_button = pygame_gui.elements.UIButton(pygame.Rect((self.x / 3 + 20, self.y / 3 + 60), (190, 90)), text = '', manager = resume_manager)   # resume text
            resume_text = self.create_text(sett_surface, "Resume", 24, 0, 0)
            resume_rect = resume_text.get_rect(center=(self.x / 3 + 112, self.y / 3 + 105))
            all_text.append(resume_text)
            all_text_rect.append(resume_rect)
            all_managers.append(resume_manager)
            all_buttons.append(resume_button)

            exit_manager = pygame_gui.UIManager((self.x, self.y), 'sky_theme.json')
            exit_button = pygame_gui.elements.UIButton(pygame.Rect((self.x / 3 + 225, self.y / 3 + 60), (190, 90)), text = '', manager = exit_manager)  # exit text
            exit_text = self.create_text(sett_surface, "Exit", 24, 0, 0)
            exit_rect = exit_text.get_rect(center=(self.x / 3 + 318, self.y / 3 + 105))
            all_text.append(exit_text)
            all_text_rect.append(exit_rect)
            all_managers.append(exit_manager)
            all_buttons.append(exit_button)

        # Blit gui
        self.window_surface.blit(sett_surface_bg, (self.x / 3, self.y / 3 - 20))
        self.window_surface.blit(sett_surface, (self.x / 3 + border_size, self.y / 3 + border_size - 20))

    # Removes access buttons from settings gui
    def remove_access_buttons(self, all_buttons, all_managers):
        if len(all_buttons) > 1:
            all_buttons.pop()   # Remove the two buttons from list so they won't continue to be updated
            all_buttons.pop()
            all_managers.pop()
            all_managers.pop()
