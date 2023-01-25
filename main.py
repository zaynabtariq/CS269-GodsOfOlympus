"""
Gods of Olympus
Last Modified: 1/24/23
Course: CS269
File: main.py
"""

##################### Setup #####################

# Import relevant classes & initialize pygame 
import pygame
import pygame_gui
from Game import Game
from titleScreen import titleScreen
from helperUI import helperUI
from charSelect import charSelect
from pygame.locals import *
import sys
pygame.init()


##################### Basic variable setups #####################

# Character variables (determines which character the game should start with)
p1_character = 1
p2_character = 2
map_type = 1

# Game class variables
HEIGHT = 750
WIDTH = 1300
ACC = 0.5
FRIC = -0.12
FPS = 60
game = Game(False, HEIGHT, WIDTH, ACC, FRIC, FPS, p1_character, p2_character, map_type)

# TitleScreen class variables
x = WIDTH    # x-dimension (screen width)
y = HEIGHT     # y-dimension (screen height)
window_surface = pygame.display.set_mode((x, y))    # Creates screen surface & background
tscreen = titleScreen(x, y, window_surface)

# charSelect class variables
char_image_size = 500   # Size of character image on character select screen
charSelectScreen = charSelect(x, y, window_surface, char_image_size)

# Button GUI variables
helper_ui = helperUI(x, y, window_surface)
character_gui_enabled = False
control_gui_enabled = False
settings_gui_enabled = False

# Start running the title screen
background = tscreen.initializeTitleScreen()
clock = pygame.time.Clock()
is_running = True
all_buttons, all_managers = tscreen.createAllButtons() 


##################### Methods #####################

# Runs the main game after pressing "Play"
def initiate_game():
    game.runGame(1)

# Resets the titleScreen after game is returned to menu
def reset_screen():
    background = tscreen.initializeTitleScreen()
    clock = pygame.time.Clock()
    all_buttons, all_managers = tscreen.createAllButtons() 
    game = Game(False, HEIGHT, WIDTH, ACC, FRIC, FPS, p1_character, p2_character, map_type)


##################### Main method #####################

# Constant updating while loop
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        #print('event.type =', event.type)  # Prints event type —- helpful for testing
        # What to do if each button is pressed
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == all_buttons[0]:      # Play button
                print('Starting game...')
                initiate_game()
                #reset_screen()      # If returned, reset title screen

            elif event.ui_element == all_buttons[1]:    # Character select button
                print('Selecting character...')
                charSelectScreen.initialize_char_select()   # Character select background
                p1_character, p2_character, map_type = charSelectScreen.loop_for_characters() # Loop until characters are selected and screen is closed
                tscreen.initializeTitleScreen()
                game = Game(False, HEIGHT, WIDTH, ACC, FRIC, FPS, p1_character, p2_character, map_type)
                break   

            elif event.ui_element == all_buttons[2]:    # Freeplay button
                print('Entering freeplay...')
                game = Game(True, HEIGHT, WIDTH, ACC, FRIC, FPS, p1_character, p2_character, map_type)
                initiate_game()
                #reset_screen()

            elif event.ui_element == all_buttons[3]:    # Controls button
                print('Checking control panel...')
                if control_gui_enabled:
                    control_gui_enabled = False
                else:
                    control_gui_enabled = True

            elif event.ui_element == all_buttons[4]:    # Settings button
                print('Opening settings...') 
                if settings_gui_enabled:
                    helper_ui.remove_access_buttons(all_buttons, all_managers)
                    settings_gui_enabled = False
                else:
                    settings_gui_enabled = True

            elif len(all_buttons) > 5 and event.ui_element == all_buttons[5]:   # Resume button
                print('Resuming game...')
                helper_ui.remove_access_buttons(all_buttons, all_managers)
                settings_gui_enabled = False

            elif len(all_buttons) > 6 and event.ui_element == all_buttons[6]:   # Exit button
                print('Exiting game...') 
                pygame.quit()
                sys.exit()

        # Update events (button hovering or clicking)
        for manager in all_managers:
            manager.process_events(event)
            manager.update(time_delta)
    
    # Update background
    window_surface.blit(background, (0, 0))
    if control_gui_enabled:
        helper_ui.initialize_control_gui()
    elif settings_gui_enabled:
        helper_ui.initialize_settings_gui(False, all_buttons, all_managers)

    # Draw buttons
    for manager in all_managers:
        manager.draw_ui(window_surface)

    # Add gear to settings button
    gear = pygame.image.load("Images/gear.png").convert_alpha()
    tscreen.color_surface(gear, 0, 201, 255)
    gear_scaled = pygame.transform.scale(gear, (40, 40))
    window_surface.blit(gear_scaled, (x - 50, 10))

    pygame.display.update()