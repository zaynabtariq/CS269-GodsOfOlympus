"""
Gods of Olympus
Last Modified: 1/17/23
Course: CS269
File: main.py
"""

##################### Setup #####################

# Import relevant classes & initialize pygame 
import pygame
import pygame_gui
from Game import Game
from fighter import Fighter
from titleScreen import titleScreen
from pygame.locals import *
import sys
pygame.init()


##################### Basic variable setups #####################

# Game class variables
HEIGHT = 750
WIDTH = 1300
ACC = 0.5
FRIC = -0.12
FPS = 60
game = Game(HEIGHT, WIDTH, ACC, FRIC, FPS)

# TitleScreen class variables
x = 1300    # x-dimension (screen width)
y = 750     # y-dimension (screen height)
window_surface = pygame.display.set_mode((x, y))    # Creates screen surface & background
tscreen = titleScreen(x, y, window_surface)

# Button GUI variables
character_gui_enabled = False
control_gui_enabled = False
settings_gui_enabled = False

# Character variables
p1_character = 1
p2_character = 2


##################### Methods #####################

# Runs the main game after pressing "Play"
def initiate_game():
    game.runGame()

# Brings up controls gui
def initialize_controls_gui(gui_enabled):
    if gui_enabled == False:
        contr_surface_bg = pygame.Surface((x / 2, y / 2 + 30))
        contr_surface_bg.fill("#21282D")

        contr_surface = pygame.Surface((x / 2 - 6, y / 2 + 30 - 6))
        contr_surface.fill("#4B5052")

        ## Add control guis here!

        window_surface.blit(contr_surface_bg, (x / 4, y / 32))
        window_surface.blit(contr_surface, (x / 4 + 3, y / 32 + 3))

        print("control gui enabled")
        return True
    else:
        tscreen.initializeTitleScreen()
        print("control gui disabled")
        return False


##################### Main method #####################

# Start running the title screen
tscreen.initializeTitleScreen()
clock = pygame.time.Clock()
is_running = True
all_buttons, all_managers = tscreen.createAllButtons()

# Constant updating while loop
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # What to do if each button is pressed
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == all_buttons[0]:
                print('Starting game...')
                initiate_game()
            elif event.ui_element == all_buttons[1]:
                print('Selecting character...')
            elif event.ui_element == all_buttons[2]:
                print('Entering freeplay...')
            elif event.ui_element == all_buttons[3]:
                print('Checking control panel...')
                control_gui_enabled = initialize_controls_gui(control_gui_enabled)
            elif event.ui_element == all_buttons[4]:
                print('Opening settings...') 

        # Update events (button hovering or clicking)
        for manager in all_managers:
            manager.process_events(event)
            manager.update(time_delta)

    
    # Draw buttons
    for manager in all_managers:
        manager.draw_ui(window_surface)

    # Add gear to settings button
    gear = pygame.image.load("gear.png").convert_alpha()
    tscreen.color_surface(gear, 200, 200, 200)
    gear_scaled = pygame.transform.scale(gear, (40, 40))
    window_surface.blit(gear_scaled, (x - 50, 10))

    pygame.display.update()
