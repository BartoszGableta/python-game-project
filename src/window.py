from typing import Tuple
import pygame
from src.characters import Player
from src.tools import EnemyGenerator

DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (0, 0)
DEFAULT_PLAYER_SPEED = 3.5
DEFAULT_PLAYER_ROTATE = 2

DEFAULT_ENEMY_SIZE = (50, 50)
DEFAULT_ENEMY_SPEED = 3

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

def handle_key_pressed(player: Player) -> None:
    """
    Handles pressing the keys by the player
    """
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.rotate_left(DEFAULT_PLAYER_ROTATE)
    if keys[pygame.K_RIGHT]:
        player.rotate_right(DEFAULT_PLAYER_ROTATE)

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

    # Sprite groups
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)

    enemy_generator = EnemyGenerator(125, player, 450, 600, window)

    # Clock
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        handle_key_pressed(player)

        x, y = player.position

        display_background(window, background_image, (-(x % WINDOW_WIDTH), -(y % WINDOW_HEIGHT)))

        if pygame.time.get_ticks() - start_time >= 500:
            enemy_generator.generate_enemy(DEFAULT_ENEMY_SIZE, DEFAULT_ENEMY_SPEED, "assets/enemy.png")
            start_time = pygame.time.get_ticks()

        enemy_generator.run()
        player_group.draw(window)
        player_group.update()

        pygame.display.update()

        clock.tick(60)
