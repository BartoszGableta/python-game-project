from typing import Tuple
import pygame
from src.characters import Player

DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (0, 0)
DEFAULT_PLAYER_SPEED = 2

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def add_player(player, window) -> None:
    """
    This function adds the ship the player controls to the window
    player: Player,
    window: _
    """

    players_spaceship = pygame.transform.scale(player.image, player.size)

    # Calculating center of the screen for displaying player model
    x_player = WINDOW_WIDTH / 2 - DEFAULT_PLAYER_SIZE[0] / 2
    y_player = WINDOW_HEIGHT / 2 - DEFAULT_PLAYER_SIZE[1] / 2

    window.blit(players_spaceship, (x_player, y_player))

def fill_surrounding_chunks(window, background, offset):
    """
    This function fills the background for area surrounding the player
    """
    off_x, off_y = offset

    window.fill((0, 0, 0))

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = dx * WINDOW_WIDTH + off_x
            y = dy * WINDOW_HEIGHT + off_y
            window.blit(background, (x, y))

def check_if_the_player_is_moving(player, event) -> None:
    """
    The function checks whether the player has pressed 
    the movement button
    """
    move_up = False
    move_down = False
    move_left = False
    move_right = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            move_left = True
        if event.key == pygame.K_RIGHT:
            move_right = True
        if event.key == pygame.K_UP:
            move_up = True
        if event.key == pygame.K_DOWN:
            move_down = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            move_left = False
        if event.key == pygame.K_RIGHT:
            move_right = False
        if event.key == pygame.K_UP:
            move_up = False
        if event.key == pygame.K_DOWN:
            move_down = False
    
    player.movement = (move_left, move_up, move_right, move_down) 
    player.move()


def create_window() -> None:
    """
    Initialize the pygame, creates the window 
    and starts game loop
    """

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Space survivor")
    #set_icon("spaceship.png")
    
    player = Player(DEFAULT_PLAYER_SIZE, DEFAULT_PLAYER_POSITION, DEFAULT_PLAYER_SPEED, "assets/spaceship.png")


    # Loading the background image
    background_image = pygame.image.load("assets/background.png").convert()
    background_image = pygame.transform.scale(background_image,(WINDOW_WIDTH, WINDOW_HEIGHT))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            check_if_the_player_is_moving(player, event)
            
        x, y = player.position

        fill_surrounding_chunks(window, background_image, (-x, -y))

        add_player(player, window)
        pygame.display.update()
