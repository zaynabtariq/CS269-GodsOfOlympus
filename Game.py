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
                        # TODO music
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load('Game_sounds/Title_music.wav')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.3)
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

    def win_screen(self, winner):

        # Stop the game loop
        self.is_running = False

        # Make background semi-transparent
        transparent_surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        transparent_surface.set_alpha(220)
        dark_screen = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(transparent_surface, (0, 0, 0), dark_screen)
        self.screen.blit(transparent_surface, (0, 0))

        # Determine winning character
        if winner == 1:
            winning_character = 'zeus'
        elif winner == 2:
            winning_character = 'hades'
        elif winner == 3:
            winning_character = 'poseidon'

        # Display the winner name
        font = pygame.font.Font(None, 48)
        text = font.render(winning_character.capitalize() + " wins!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
        self.screen.blit(text, text_rect)

        winner_img = pygame.image.load(f'Images/{winning_character}main.png')
        winner_img = pygame.transform.scale(winner_img, (winner_img.get_width() * 2, winner_img.get_height() * 2))
        self.screen.blit(winner_img, (self.WIDTH/2-190, self.HEIGHT/2 - 350))

        # Display options
        font = pygame.font.Font(None, 32)
        play_again_text = font.render("Play Again", True, (255, 255, 255))
        play_again_rect = play_again_text.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 + 50))
        self.screen.blit(play_again_text, play_again_rect)

        exit_text = font.render("Exit", True, (255, 255, 255))
        exit_rect = exit_text.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2 + 100))
        self.screen.blit(exit_text, exit_rect)

        pygame.display.update()

        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_rect.collidepoint(event.pos):
                        # reset the number of rounds won for each player
                        self.f1_wins = 0
                        self.f2_wins = 0
                        # restart the game loop
                        self.is_running = True
                        waiting = False

                        pygame.mixer.music.unload()
                        pygame.mixer.music.load('Game_sounds/Background_music.wav')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.3)

                    elif exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                        pygame.mixer.music.unload()
                        pygame.mixer.music.load('Game_sounds/Title_music.wav')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.3)

    # Loads the "rounds" screen
    def loadRounds(self, round_num):
        # Font settings
        font = pygame.font.Font(None, 36)
        self.screen.fill((0, 0, 0))

        # Draw the background screen with the round number text TODO tomorrow
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        img_bg = pygame.image.load('Images/sky_palace.jpg')
        img_bg = pygame.transform.scale(img_bg, (self.WIDTH, self.HEIGHT))

        img_round = pygame.image.load(f'Images/round_{round_num}.png')
        img_round = pygame.transform.scale(img_round, (img_round.get_width() * 3, img_round.get_height() * 3))

        img_center = (self.WIDTH/2-550, self.HEIGHT/2-330)

        self.screen.blit(img_bg, (0, 0))
        self.screen.blit(img_round, img_center)

        # Update the display
        pygame.display.flip()

        # Wait 2 seconds before continuing
        pygame.time.wait(2000)

        # Remove the semi-transparent screen
        self.screen.fill((0, 0, 0))

    # Runs the game
    def runGame(self, round_num):
        
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
        pygame.mixer.music.load('Game_sounds/Background_music.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        # Font settings
        if self.is_freeplay == False:   
            self.loadRounds(round_num)

        # game looper
        while True:

            if self.return_to_menu:
                return

            # checks if a fighter has no hp and restarts the game if that's the case
            if fighter_1.health <= 0 or fighter_2.health <= 0:
                round_num += 1
                if fighter_1.health <= 0:
                    self.f2_wins += 1     # fighter 2 earns a round

                    if self.f2_wins == 3:
                        round_num = 1
                        self.win_screen(self.p2_character) # if fighter 2 wins three rounds, end game

                else:
                    self.f1_wins += 1     # fighter 1 earns a round

                    if self.f1_wins == 3:
                        round_num = 1
                        self.win_screen(self.p1_character) # if fighter 1 wins three rounds, end game


                pygame.time.wait(1500)
                self.runGame(round_num)

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
            if self.is_freeplay == False:   
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
