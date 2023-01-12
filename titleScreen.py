"""
Gods of Olympus
Last Modified: 1/11/23 by jctjad
Course: CS269
File: titleScreen.py
"""

import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption('Title Screen')

x = 1300    # x-dimension (screen width)
y = 750     # y-dimension (screen height)

window_surface2 = pygame.display.set_mode((60, 60))
window_surface = pygame.display.set_mode((x, y))
background = pygame.Surface((x, y))
background.fill(pygame.Color('#999999'))


# Creates all main buttons
def createAllButtons():

    # Method to make a standard button
    def makeStandardButton(location_y, the_text, the_manager):
        button = pygame_gui.elements.UIButton(pygame.Rect((location_x, location_y), (size_x, size_y)), text = the_text, manager = the_manager)
        button_background = pygame.Rect((location_x - border_size, location_y - border_size), (size_x + (2 * border_size), size_y + (2 * border_size)))
        return button, button_background

    # Method to make the settings button
    def makeSettingsButton(the_manager):
        settings_button = pygame_gui.elements.UIButton(pygame.Rect((settings_location_x, settings_location_y), (settings_size, settings_size)), text = '', manager = the_manager)
        settings_button_background = pygame.Rect((settings_location_x - border_size, settings_location_y - border_size), (settings_size + (2 * border_size), settings_size + (2 * border_size)))
        return settings_button, settings_button_background


    # Standard button variables
    size_x = 200
    size_y = 50
    location_x = (x / 2) - (size_x / 2)
    location_y = (y / 2) + (size_y / 2) + 60    # 60 is changeable pixel amount for the height of the buttons
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
        manager = pygame_gui.UIManager((x, y), 'button.json')   # Where x and y are background dimensions
        all_managers.append(manager)

    # Button 1 ('Play' button)
    button_1_y = location_y     # location_y of button_1
    button_1, button_1_background = makeStandardButton(button_1_y, 'Play', all_managers[0])

    # Button 2 ('Character select' button)
    button_2_y = button_1_y + space_inbetween_buttons    # Adding size_y to account for first button size. Unnecessary for following buttons
    button_2, button_2_background = makeStandardButton(button_2_y, 'Character Select', all_managers[1])

    # Button 3 ('Freeplay' button)
    button_3_y = button_2_y + space_inbetween_buttons
    button_3, button_3_background = makeStandardButton(button_3_y, 'Freeplay', all_managers[2])

    # Button 4 ('Controls' button)
    button_4_y = button_3_y + space_inbetween_buttons
    button_4, button_4_background = makeStandardButton(button_4_y, 'Controls', all_managers[3])

    # Button 5 ('Settings' button) -> unique location
    button_5, button_5_background = makeSettingsButton(all_managers[4])

    all_buttons = [button_1, button_2, button_3, button_4, button_5]
    all_button_backgrounds = [button_1_background, button_2_background, button_3_background, button_4_background, button_5_background]

    return all_buttons, all_button_backgrounds, all_managers


# Back to main function...

clock = pygame.time.Clock()
is_running = True
all_buttons, all_button_backgrounds, all_managers = createAllButtons()

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

    # Update window_surface
    window_surface.blit(background, (0, 0))

    # Draw button backgrounds
    background_color = '#333333'
    for button_background in all_button_backgrounds:
        pygame.draw.rect(window_surface, pygame.Color(background_color), button_background)

    # Draw buttons
    for manager in all_managers:
        manager.draw_ui(window_surface)

    # Add gear to settings button
    gear = pygame.image.load("gear2.png").convert_alpha()
    gear_scaled = pygame.transform.scale(gear, (40, 40))
    window_surface.blit(gear_scaled, (x - 50, 10))

    pygame.display.update()

