DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (300, 300)
DEFAULT_PLAYER_SPEED = 5

import pygame
from typing import Tuple
from characters import Player

def add_player(player, window) -> None:
    """
    This function adds the ship the player controls to the window
    player: Player,
    window: _
    """

    players_spaceship = pygame.transform.scale(player.image, player.size)
    window.blit(players_spaceship, player.position)


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
    window = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Space survivor")
    #set_icon("spaceship.png")
    
    player = Player(DEFAULT_PLAYER_SIZE, DEFAULT_PLAYER_POSITION, DEFAULT_PLAYER_SPEED, "spaceship.png")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            check_if_the_player_is_moving(player, event)
        
        window.fill((0,0,0)) # Sets the window colour according to RGB
        add_player(player, window)
        pygame.display.update() 
