"""
Gods of Olympus
Last Modified: 1/15/23 by jctjad
Course: CS269
File: titleScreen.py
"""

##################### Setup #####################

import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption('Title Screen')

x = 1300    # x-dimension (screen width)
y = 750     # y-dimension (screen height)

# Create screen surface & background
window_surface = pygame.display.set_mode((x, y))

background = pygame.Surface((x, y))
background.fill(pygame.Color('#88c8ee'))
sky_image = pygame.image.load("sky.webp").convert_alpha()
background.blit(sky_image, (0, 0))


##################### Methods #####################

# Creates all main buttons
def createAllButtons():

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
    location_x = (x / 2) - (size_x / 2)
    location_y = (y / 2) + (size_y / 2) + 55    # 55 is changeable pixel amount for the height of the buttons
    space_inbetween_buttons = size_y + (size_y / 2)
    border_size = 1

    # Settings button variables
    settings_size = 40
    distance_from_edge = 10
    settings_location_x = x - settings_size - distance_from_edge
    settings_location_y = distance_from_edge

    # Define button managers
    all_managers = []
    for i in range(0, 5):
        manager = pygame_gui.UIManager((x, y), 'button.json')   # Where x and y are background dimensions, and button.json is the button theme
                                                                # If button.json isn't working on your computer just delete it (theme is optional)
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
def color_surface(surface, red, green, blue):
    arr = pygame.surfarray.pixels3d(surface)
    arr[:,:,0] = red
    arr[:,:,1] = green
    arr[:,:,2] = blue


##################### Back to main function #####################

clock = pygame.time.Clock()
is_running = True
all_buttons, all_managers = createAllButtons()

# Add the background to the surface
window_surface.blit(background, (0, 0))

# Add characters to screen
fighter_image_size = 500

fighter_1_image = pygame.image.load("zeus_front.png").convert_alpha()
fighter_1_art = pygame.transform.scale(fighter_1_image, (fighter_image_size, fighter_image_size))
fighter_2_image = pygame.image.load("zeus_side.png").convert_alpha()
fighter_2_image = pygame.transform.flip(fighter_2_image, True, False)   # Flip surface horizontally
fighter_2_art = pygame.transform.scale(fighter_2_image, (fighter_image_size, fighter_image_size))

background.blit(fighter_1_art, (-100, y / 5))
background.blit(fighter_2_art, (x - fighter_image_size + 100, y / 5))

# Add logo/text/image
image_size_x = 700
image_size_y = 400

center_image = pygame.image.load("logo.png").convert_alpha()
center_image = pygame.transform.scale(center_image, (image_size_x, image_size_y))
background.blit(center_image, ((x - image_size_x) / 2, 0))

# Update background
window_surface.blit(background, (0, 0))

# Constant updating while loop
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # What to do if each button is pressed
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == all_buttons[0]:
                print('Starting game...')           ## This is where we can call the Game class
            elif event.ui_element == all_buttons[1]:
                print('Selecting character...')
            elif event.ui_element == all_buttons[2]:
                print('Entering freeplay...')
            elif event.ui_element == all_buttons[3]:
                print('Checking control panel...')
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
    color_surface(gear, 200, 200, 200)
    gear_scaled = pygame.transform.scale(gear, (40, 40))
    window_surface.blit(gear_scaled, (x - 50, 10))

    pygame.display.update()
