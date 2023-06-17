import pygame
import src.const as const

from typing import Tuple
from src.entities import Player
from src.tools import EnemyGenerator

def display_background(window: pygame.Surface, background: pygame.Surface, offset: Tuple[int, int]) -> None:
    """
    This function fills the background for area surrounding the player
    """
    off_x, off_y = offset

    window.fill((0, 0, 0))

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = dx * const.WINDOW_WIDTH + off_x
            y = dy * const.WINDOW_HEIGHT - off_y
            window.blit(background, (x, y))

def handle_key_pressed(player: Player) -> None:
    """
    Handles pressing the keys by the player
    """
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.rotate_left(const.DEFAULT_PLAYER_ROTATE)
    if keys[pygame.K_RIGHT]:
        player.rotate_right(const.DEFAULT_PLAYER_ROTATE)

def create_window() -> None:
    """
    Initialize the pygame, creates the window 
    and starts game loop
    """

    window = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

    pygame.display.set_caption(const.WINDOW_NAME)
    
    player = Player(const.DEFAULT_PLAYER_SIZE, const.DEFAULT_PLAYER_POSITION, const.DEFAULT_PLAYER_SPEED, const.PLAYER_IMAGE)

    # Loading the background image
    background_image = pygame.image.load(const.GAME_BACKGROUND).convert()
    background_image = pygame.transform.scale(background_image,(const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

    # Sprite groups
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)

    enemy_generator = EnemyGenerator(
        const.DEFAULT_ENEMY_LIMIT, 
        player, 
        const.ENEMY_GENERATION_DISTANCE, 
        const.ENEMY_MAX_DISTANCE, 
        window)

    # Clock
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        
        handle_key_pressed(player)

        x, y = player.position

        display_background(window, background_image, (-(x % const.WINDOW_WIDTH), -(y % const.WINDOW_HEIGHT)))

        if pygame.time.get_ticks() - start_time >= const.GENERATION_TIME:
            enemy_generator.generate_enemy(const.DEFAULT_ENEMY_SIZE, const.DEFAULT_ENEMY_SPEED, const.PLAYER_IMAGE)
            start_time = pygame.time.get_ticks()

        enemy_generator.run()
        player_group.draw(window)
        player_group.update()

        pygame.display.update()

        clock.tick(60)
