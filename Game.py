"""
Gods of Olympus
Last Modified: 1/24/23
Course: CS269
File: Game.py
"""

import pygame
import pygame_gui
from pygame import mixer
from Zeus import Zeus
from Hades import Hades
from Poseidon import Poseidon
from helperUI import helperUI
from map import Map
from pygame.locals import *
import sys

class Game():

    # Constructor
    def __init__(self, is_freeplay, HEIGHT, WIDTH, ACC, FRIC, FPS, p1_character, p2_character, map_type):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.ACC = ACC
        self.FRIC = FRIC
        self.FPS = FPS
        self.f1_wins = 0
        self.f2_wins = 0
        self.FramePerSec = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.p1_character = p1_character
        self.p2_character = p2_character
        self.is_running = True
        self.is_freeplay = is_freeplay
        self.return_to_menu = False

        # Settings button
        self.paused = False
        self.settings_manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT), 'sky_theme.json')
        self.settings_button = pygame_gui.elements.UIButton(pygame.Rect((self.WIDTH - 50, 10), (40, 40)), text = '', manager = self.settings_manager)        
        self.settings_gui_enabled = False                                           
        self.helper_ui = helperUI(self.WIDTH, self.HEIGHT, self.screen)

        # load map
        self.map = Map(map_type, HEIGHT, WIDTH, ACC, FRIC, FPS, self.screen)

        #define fighter variables
        self.ledges = self.map.draw_ledges()

        #test

    # Colors all visible pixels of an image
    def color_surface(self, surface, red, green, blue):
        arr = pygame.surfarray.pixels3d(surface)
        arr[:,:,0] = red
        arr[:,:,1] = green
        arr[:,:,2] = blue

    # Resumes the game
    def resumeGame(self, buttons, managers):
        print('Resuming game...')
        self.helper_ui.remove_access_buttons(buttons, managers)
        self.is_running = False

    # Pauses the game
    def pauseGame(self):

        print('GAME PAUSED!')
        clock = pygame.time.Clock()
        self.is_running = True

        # Make background semi-transparent
        transparent_surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        transparent_surface.set_alpha(128)
        dark_screen = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(transparent_surface, (0, 0, 0), dark_screen)
        self.screen.blit(transparent_surface, (0, 0))
        
        # Initialize Settings GUI
        buttons = []
        managers = []
        self.helper_ui.initialize_settings_gui(True, buttons, managers)

        # Update display
        pygame.display.update()
        
        while self.is_running:
            time_delta = clock.tick(60)/1000.0
            key = pygame.key.get_pressed()
            for event in pygame.event.get():  
                if key[pygame.K_ESCAPE] or key[pygame.K_p]:
                    self.is_running = False

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:  # What to do if each button is pressed
                    if event.ui_element == buttons[0]:      # Resume button
                        print('Resuming game...')
                        self.resumeGame(buttons, managers)
                        #self.is_running = False
                        break
                        
                    elif event.ui_element == buttons[1]:    # Exit button
                        print('Exiting game...')
                        self.return_to_menu = True  # Return to menu
                        return
                    
                # Update events (button hovering or clicking)
                for manager in managers:
                    manager.process_events(event)
                    manager.update(time_delta)
            
            # Update screen
            self.helper_ui.initialize_settings_gui(True, buttons, managers)

            # Draw buttons
            for manager in managers:
                manager.draw_ui(self.screen)

            pygame.display.update()

    # Runs the game
    def runGame(self):
        
        # starting location of fighters
        if self.p1_character == 1:
            fighter_1 = Zeus(1, 0, self.HEIGHT - 200, self.ledges, self.screen)
        elif self.p1_character == 2:
            fighter_1 = Hades(1, 0, self.HEIGHT - 200, self.ledges, self.screen)
        elif self.p1_character == 3:
            fighter_1 = Poseidon(1, 0, self.HEIGHT - 200, self.ledges, self.screen)
        else:
            fighter_1 = Zeus(1, 0, self.HEIGHT - 200, self.ledges, self.screen)

        if self.p2_character == 1:
            fighter_2 = Zeus(2, self.WIDTH - 400, self.HEIGHT-500, self.ledges, self.screen)
        elif self.p2_character == 2:
            fighter_2 = Hades(2, self.WIDTH - 400, self.HEIGHT-500, self.ledges, self.screen)
        elif self.p2_character == 3:
            fighter_2 = Poseidon(2, self.WIDTH - 400, self.HEIGHT-500, self.ledges, self.screen)
        else:
            fighter_2 = Hades(2, self.WIDTH - 400, self.HEIGHT - 500, self.ledges, self.screen)

        # Sets screen header
        pygame.display.set_caption("Gods of Olympus")

        # Load music
        pygame.mixer.music.unload()
        #pygame.mixer.music.load('Game_sounds/Background_music.wav')
        #pygame.mixer.music.play(-1)
        #pygame.mixer.music.set_volume(0.3)

        # game looper
        while True:

            if self.return_to_menu:
                return

            # checks if a fighter has no hp and restarts the game if that's the case
            if fighter_1.health <= 0 or fighter_2.health <= 0:
                if fighter_1.health <= 0:
                    self.f2_wins += 1     # fighter 2 earns a round
                else:
                    self.f1_wins += 1     # fighter 1 earns a round
                pygame.time.wait(1500)
                self.runGame()

            # draw background
            self.map.draw_bg()
            self.ledges = self.map.draw_ledges()

            # move fighters
            fighter_1.move(self.WIDTH, self.HEIGHT, fighter_2, self.screen, self.ledges)
            fighter_2.move(self.WIDTH, self.HEIGHT, fighter_1, self.screen, self.ledges)

            # draw fighters
            fighter_1.update(fighter_2)
            fighter_2.update(fighter_1)
            fighter_1.draw(self.screen)
            fighter_2.draw(self.screen)

            # draw hp bar for fighters
            self.map.draw_health_bars(fighter_1.health, 'fighter_2')
            self.map.draw_health_bars(fighter_2.health, 'fighter_1')
            self.map.draw_score_icons(self.p1_character, self.p2_character) # draw icons of idols

            # Draws scoreboard
            self.map.draw_stats(self.f1_wins, self.f2_wins)

            # allows player to exit
            key = pygame.key.get_pressed() 
            for event in pygame.event.get():
                if event.type == QUIT:  # Quits game
                    pygame.quit()
                    sys.exit()
                if key[pygame.K_ESCAPE] or key[pygame.K_p]:     # Pauses game
                    self.pauseGame()
                    
            # Update display
            pygame.display.update()
            self.FramePerSec.tick(self.FPS)
