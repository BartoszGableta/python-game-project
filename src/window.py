import pygame
import src.const as const

from typing import Tuple

from src.tools import EnemyGenerator, PointsCounter
from src.entities import Player, Enemy, Bullet, Character
from src.collisions import check_collisions, check_player_bullet_hits, check_enemies_bullet_hits


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
    
def set_timer(time, callback):
    start = 0
    def timer():
        nonlocal start
        if pygame.time.get_ticks() - start > time:
            callback()
            start = pygame.time.get_ticks()
    return timer

def create_window() -> None:
    """
    Initialize the pygame, creates the window 
    and starts game loop
    """

    window = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))

    pygame.display.set_caption(const.WINDOW_NAME)
    

    players_bullet = (
        const.DEFAULT_PLAYER_BULLET_SPEED, 
        const.DEFAULT_PLAYER_BULLET_DAMAGE, 
        const.DEFAULT_PLAYER_BULLET_SIZE, 
        const.PLAYER_BULLET_IMAGE
        )
    
    player = Player(
        const.DEFAULT_PLAYER_SIZE, 
        const.DEFAULT_PLAYER_POSITION, 
        const.DEFAULT_PLAYER_SPEED, 
        const.PLAYER_IMAGE, 
        0, 
        const.DEFAULT_PLAYER_HP, 
        players_bullet
        )

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
        window,
        const.DEFAULT_ENEMY_HP)

    players_bullets = pygame.sprite.Group()
    enemies_bullets = pygame.sprite.Group()

    # Clock
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load(const.GAME_MUSIC)
    pygame.mixer.music.set_volume(const.MUSIC_VOLUME)
    pygame.mixer.music.play(loops=-1)

    # Counter
    counter = PointsCounter()

    # Timers
    player_bullet_timer = set_timer(150, lambda : new_bullet(player, players_bullets))
    enemy_bullet_timer = set_timer(300, lambda : new_bullet_for_group(enemy_generator.enemies, enemies_bullets))
    enemy_generation_timer = set_timer(
        1000, 
        lambda : enemy_generator.generate_enemy(const.DEFAULT_ENEMY_SIZE, const.DEFAULT_ENEMY_SPEED, const.ENEMY_IMAGE)
        )

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

        player_bullet_timer()
        enemy_bullet_timer()
        enemy_generation_timer()

        counter.update_and_draw(window)

        players_bullets.draw(window)
        players_bullets.update(player)

        enemies_bullets.draw(window)
        enemies_bullets.update(player)

        enemy_generator.run()
        player_group.draw(window)
        player_group.update()
        
        check_collisions(player, enemy_generator.enemies, lambda : counter.update_and_draw(window, const.KILL_POINTS))
        check_player_bullet_hits(players_bullets, enemy_generator.enemies, lambda : counter.update_and_draw(window, const.KILL_POINTS))
        
        if check_enemies_bullet_hits(enemies_bullets, player):
            running = False
            return counter.points

        pygame.display.update()

        clock.tick(60)

