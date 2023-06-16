from typing import Tuple
import pygame
from src.entities import Player, Enemy

DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (0, 0)
DEFAULT_PLAYER_SPEED = .2
DEFAULT_PLAYER_ROTATE = 0.2

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def display_background(window: pygame.Surface, background: pygame.Surface, offset: Tuple[int, int]) -> None:
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

    #TODO Test entity [for future removal]
    ent = Enemy((80, 80), (-200, -200), 0.1, "assets/enemy.png")
    ent2 = Enemy((80, 80), (200, 200), 0.1, "assets/enemy.png")
    ent3 = Enemy((80, 80), (-300, 300), 0.1, "assets/enemy.png")
    

    # Sprite groups
    player_group = pygame.sprite.Group()
    player_group.add(player)

    enemies_group = pygame.sprite.Group()
    enemies_group.add(ent, ent2, ent3)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.rotate_left(DEFAULT_PLAYER_ROTATE)
        if keys[pygame.K_RIGHT]:
            player.rotate_right(DEFAULT_PLAYER_ROTATE)

        x, y = player.position

        display_background(window, background_image, (-(x % WINDOW_WIDTH), -(y % WINDOW_HEIGHT)))
        
        enemies_group.draw(window)
        enemies_group.update(player)
        player_group.draw(window)
        player_group.update()


        pygame.display.update()
