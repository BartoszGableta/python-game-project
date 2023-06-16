import pygame

DEFAULT_DAMAGE_POINTS = 5

def check_collisions(sprite_player, sprites):
    gets_hit = pygame.sprite.spritecollide(sprite_player, sprites, False, pygame.sprite.collide_mask)
    for enemy in gets_hit:
        enemy.stop_collisions(sprite_player.speed, sprite_player.angle)
        sprite_player.stop_collisions(enemy.speed, enemy.angle)
        sprite_player.damage(DEFAULT_DAMAGE_POINTS)
        enemy.damage(DEFAULT_DAMAGE_POINTS)
