from typing import Tuple
import pygame
from src.characters import Player, Enemy

DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (0, 0)
DEFAULT_PLAYER_SPEED = .3
DEFAULT_PLAYER_ROTATE = 0.5

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def add_player(player, window) -> None:
    """
    This function adds the ship the player controls to the window
    player: Player,
    window: _
    """

    players_spaceship = pygame.transform.scale(player.image, player.size)   
    rotated_players_spaceship = pygame.transform.rotate(players_spaceship, player.angle)
    
    
    # Calculating center of the screen for displaying player model
    x_player = WINDOW_WIDTH / 2 - rotated_players_spaceship.get_width() / 2
    y_player = WINDOW_HEIGHT / 2 - rotated_players_spaceship.get_height() / 2

    window.blit(rotated_players_spaceship, (x_player, y_player))

def add_entity(entity, player, window):
    """
    This function adds an antity with respect to the player's position
    """

    # Creating entity image and getting it's information
    entity_image = pygame.transform.scale(entity.image, entity.size)

    rotated_entity_image = pygame.transform.rotate(entity.image, entity.angle)

    ent_width, ent_height = entity.size
    x_entity, y_entity = entity.position

    x_player, y_player = player.position

    # Calculating display position for the entity
    x_entity = (WINDOW_WIDTH / 2) + (x_entity - x_player) - rotated_entity_image.get_width() / 2
    y_entity = (WINDOW_HEIGHT / 2) - (y_entity - y_player) - rotated_entity_image.get_height() / 2

    window.blit(rotated_entity_image, (x_entity, y_entity))


def fill_surrounding_chunks(window, background, offset):
    """
    This function fills the background for area surrounding the player
    """
    off_x, off_y = offset

    window.fill((0, 0, 0))

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = dx * WINDOW_WIDTH + off_x
            y = dy * WINDOW_HEIGHT - off_y
            window.blit(background, (x, y))


def check_if_the_player_is_moving(event) -> int:
    """
    The function checks whether the player has pressed 
    the movement button and return one of the four values:
    -1 -> the player has released the button 
    0 -> the player continues to turn the ship
    1 -> the player turns right
    2 -> the players turns left
    """
    
    new_direction_of_rotation = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            new_direction_of_rotation = 2
        if event.key == pygame.K_RIGHT:
            new_direction_of_rotation = 1
    if event.type == pygame.KEYUP:
        new_direction_of_rotation = -1
    
    if event.type != pygame.KEYUP and event.type != pygame.KEYDOWN:
        new_direction_of_rotation = 0

    return new_direction_of_rotation

def rotate_the_player(player, event) -> None:
    """
    The function sets the direction of rotation for the player
    based on the button selected by the player
    """
    new_direction_of_rotation = check_if_the_player_is_moving(event)
    
    if new_direction_of_rotation == 0:
        new_direction_of_rotation = player.direction_of_rotation

    player.direction_of_rotation = new_direction_of_rotation

def create_window() -> None:
    """
    Initialize the pygame, creates the window 
    and starts game loop
    """

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Space survivor")
    
    player = Player(DEFAULT_PLAYER_SIZE, DEFAULT_PLAYER_POSITION, DEFAULT_PLAYER_SPEED, "assets/spaceship.png")


    # Loading the background image
    background_image = pygame.image.load("assets/background.png").convert()
    background_image = pygame.transform.scale(background_image,(WINDOW_WIDTH, WINDOW_HEIGHT))

    # Test entity
    ent = Enemy((40, 40), (-200, -200), 0.1, "assets/enemy.png")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            rotate_the_player(player, event)
            
        player.rotate(DEFAULT_PLAYER_ROTATE)
        player.move()
        x, y = player.position

        ent.rotate(player)
        ent.move()

        fill_surrounding_chunks(window, background_image, (-(x % WINDOW_WIDTH), -(y % WINDOW_HEIGHT)))
        add_entity(ent, player, window)
        add_player(player, window)
        pygame.display.update()
