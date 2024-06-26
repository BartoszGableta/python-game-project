import pygame
import math
import sys
from src.entities import Character
import src.const as const
from typing import Callable

def get_closest_enemy(enemies: pygame.sprite.Group):
    """
    Calculates and returns a list of opponents whose distance from the player is the smallest
    """
    min = sys.maxsize
    closest_enemies = []
    for enemy in enemies:
        if min >= (new_min:=enemy.distance_from_player):
            if min == new_min:
                closest_enemies.append(enemy)
            else:
                min = new_min
                closest_enemies = [enemy]
    
    return closest_enemies

def check_collisions(sprite_player: Character, sprites: pygame.sprite.Group, callback_when_killed=(lambda : None)):
    """
    Calculates whether there is a collision between the player and the opponents 
    (if there is it will subtract the life points of both characters that collided)
    """
    gets_hit = pygame.sprite.spritecollide(sprite_player, get_closest_enemy(sprites), False, pygame.sprite.collide_mask)
    for enemy in gets_hit:
        enemy.stop_collisions(sprite_player.speed)
        sprite_player.stop_collisions(enemy.speed)
        sprite_player.damage(const.COLLISION_DAMAGE)
        if enemy.damage(const.COLLISION_DAMAGE):
            callback_when_killed()
            

def furthest_bullet_for_angle(bullets: pygame.sprite.Group):
    """
    Calculates the bullets that are furthest from the player for each angle
    """
    max = 0
    furthest_bullets = {}
    for bullet in bullets:
        if bullet.angle in furthest_bullets:
            max_bullet = furthest_bullets[bullet.angle]
            if max_bullet.distance_from_player < bullet.distance_from_player:
                 furthest_bullets.update({bullet.angle: bullet})
        else:
            furthest_bullets.update({bullet.angle: bullet})

    return [v for v in furthest_bullets.values()]

def check_player_bullet_hits(bullets: pygame.sprite.Group, enemies: pygame.sprite.Group, callback_when_killed=(lambda : None)):
    """
    Calculates whether the player's bullets hit enemies
    """
    important_bullets = furthest_bullet_for_angle(bullets)
    for bullet in important_bullets:
        gets_hit = pygame.sprite.spritecollide(bullet, enemies, False, pygame.sprite.collide_mask)
        for hit in gets_hit:
            if hit.damage(bullet.damage):
                callback_when_killed()
            bullet.kill()


def check_enemies_bullet_hits(bullets: pygame.sprite.Group, player: Character) -> bool:
    """
    Calculates whether enemies' bullets hit the player.
    Return bool value indicating if the player is dead.
    """
    gets_hit = pygame.sprite.spritecollide(player, bullets, False, pygame.sprite.collide_mask)
    for hit in gets_hit:
        if player.damage(hit.damage):
            return True
        hit.kill()
    return False
