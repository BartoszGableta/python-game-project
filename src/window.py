from typing import Tuple
import pygame
from src.tools import EnemyGenerator, PointsCounter
from src.entities import Player, Enemy, Bullet, Character
from src.collisions import check_collisions, check_player_bullet_hits, check_enemies_bullet_hits

DEFAULT_PLAYER_SIZE = (50, 50)
DEFAULT_PLAYER_POSITION = (0, 0)
DEFAULT_PLAYER_SPEED = 3.5
DEFAULT_PLAYER_ROTATE = 2
DEFAULT_PLAYER_LIFE_POINTS = 100

DEFAULT_PLAYER_BULLET_SIZE = (10, 10)
DEFAULT_PLAYER_BULLET_SPEED = 8
DEFAULT_PLAYER_BULLET_DAMAGE = 60
DEFAULT_PLAYER_BULLET_IMAGE = "assets/bullet.png"

DEFAULT_ENEMY_SIZE = (50, 50)
DEFAULT_ENEMY_SPEED = 1

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

def new_bullet(character: Character, bullets: pygame.sprite.Group) -> None:
    """
    Adds a new bullet to the Character's bullet group
    """
    bullet = character.shot()
    bullets.add(bullet)

def new_bullet_for_group(group: pygame.sprite.Group, bullets: pygame.sprite.Group) -> None:
    """
    Adds a new bullet to the all characters from group
    """
    for character in group:
        bullet = character.shot()
        bullets.add(bullet)


def create_window() -> None:
    """
    Initialize the pygame, creates the window 
    and starts game loop
    """

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Space survivor")
    
    players_bullet = (DEFAULT_PLAYER_BULLET_SPEED, DEFAULT_PLAYER_BULLET_DAMAGE, DEFAULT_PLAYER_BULLET_SIZE, DEFAULT_PLAYER_BULLET_IMAGE)
    player = Player(DEFAULT_PLAYER_SIZE, DEFAULT_PLAYER_POSITION, DEFAULT_PLAYER_SPEED, "assets/spaceship.png", 0, DEFAULT_PLAYER_LIFE_POINTS, players_bullet)

    # Loading the background image
    background_image = pygame.image.load("assets/background.png").convert()
    background_image = pygame.transform.scale(background_image,(WINDOW_WIDTH, WINDOW_HEIGHT))

    # Sprite groups
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)

    enemy_generator = EnemyGenerator(125, player, 450, 600, window, 60)

    players_bullets = pygame.sprite.Group()
    enemies_bullets = pygame.sprite.Group()

    # Clock
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    # Counter
    counter = PointsCounter()

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

        display_background(window, background_image, (-(x % WINDOW_WIDTH), -(y % WINDOW_HEIGHT)))

        if (time := (pygame.time.get_ticks() - start_time)) % 10 == 0:
            new_bullet(player, players_bullets)
            if time % 40 == 0:
                new_bullet_for_group(enemy_generator.enemies, enemies_bullets)


        if pygame.time.get_ticks() - start_time >= 500:
            enemy_generator.generate_enemy(DEFAULT_ENEMY_SIZE, DEFAULT_ENEMY_SPEED, "assets/enemy.png")
            start_time = pygame.time.get_ticks()


        counter.update()

        players_bullets.draw(window)
        players_bullets.update(player)

        enemies_bullets.draw(window)
        enemies_bullets.update(player)

        enemy_generator.run()
        player_group.draw(window)
        player_group.update()


        counter.draw(window)
        
        check_collisions(player, enemy_generator.enemies)
        check_player_bullet_hits(players_bullets, enemy_generator.enemies)
        check_enemies_bullet_hits(enemies_bullets, player)

        pygame.display.update()

        clock.tick(60)

