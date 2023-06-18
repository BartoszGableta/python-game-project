from abc import ABC, abstractclassmethod
from typing import Tuple
import pygame
import math


class Entity(pygame.sprite.Sprite, ABC):
    """
    The class symbolises an entity which is an element that moves on the screen
    """

    def __init__(self, size: Tuple[int, int], position: Tuple[int, int], speed: int, image: str, angle: int) -> None:
        super().__init__()

        image = pygame.image.load(image).convert_alpha()
        self.orig_image = pygame.transform.scale(image, size)
        self.image = self.orig_image

        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        
        self.angle = angle
        self.position = position
        self.speed = speed
        self.angle = angle
    
    def stop_collisions(self, enemies_speed: int) -> None:
        x_change = -enemies_speed * math.sin(math.radians(self.angle))
        y_change = -enemies_speed * math.cos(math.radians(self.angle))
        self.position = (self.position[0] - x_change, self.position[1] + y_change)
        
    
    def move(self) -> None:   
        x_change = self.speed * math.sin(math.radians(self.angle))
        y_change = self.speed * math.cos(math.radians(self.angle))
        self.position = (self.position[0] - x_change, self.position[1] + y_change)
        
class Bullet(Entity):
    """
    The class symbolises the bullet that the characters shoot.
    """

    def __init__(self, size: Tuple[int, int], position: Tuple[int, int], speed: int, image: str, angle: int, damage: int) -> None:
        super().__init__(size, position, speed, image, angle)
        self.damage = damage
        self.image = pygame.transform.rotate(self.orig_image, angle+45) #+45 because the picture is rotated xdd note to change it

    def thrown_away(self, x_diff: int, y_diff: int) -> None:
        if (x_diff > 400 or x_diff < -400) or (y_diff > 300 or y_diff < -300):
            self.kill()


    def update(self, player: Entity) -> None:
        self.move()
        self.rect = self.image.get_rect()
        
        x, y = self.position
        x_off, y_off = player.position
        x_diff, y_diff = (x - x_off), (y - y_off)
        self.rect.center = (400 + x_diff, 300 - y_diff)
        self.distance_from_player = math.sqrt(x_diff**2 + y_diff**2)
        self.thrown_away(x_diff, y_diff)


class Character(Entity):
    """
    The class symbolises a character, or entity, that can inflict and receive damage
    """

    def __init__(self, size: Tuple[int, int], position: Tuple[int, int], speed: int, image: str, angle: int, life_points: int, bullet: Tuple[Tuple[int, int], int, int, str]) -> None:
        super().__init__(size, position, speed, image, angle)
        self.life_points = life_points
        self.bullet = bullet

    def is_alive(self) -> bool:
        return self.life_points > 0
    
    def damage(self, damage_points) -> bool:
        """
        Function that deals damage to a character.
        It returns a bool value indicating if the character was killed.
        """
        self.life_points -= damage_points
        if not self.is_alive():
            self.kill()
            return True
        return False
    
    def shot(self) -> Bullet:
        bullet_speed, bullet_damage, bullet_size, bullet_image = self.bullet
        return Bullet(bullet_size, self.position, bullet_speed, bullet_image, self.angle, bullet_damage)
    
    

class Player(Character):
    """
    The class symbolises the player
    """
    
    def __init__(self, size: Tuple[int, int], position: Tuple[int, int], speed: int, image: str, angle: int, life_points: int, bullet: Tuple[Tuple[int, int], int, int, str]) -> None:
        super().__init__(size, position, speed, image, angle, life_points, bullet)
        

    def rotate_left(self, rotation: int) -> None:
        self.angle =  (self.angle + rotation) % 360

    def rotate_right(self, rotation: int) -> None:
        self.angle = (self.angle - rotation) % 360

    def update(self) -> None:
        self.move()
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)


class Enemy(Character):
    """
    The class symbolises the enemy
    """

    def __init__(self, size: Tuple[int, int], position: Tuple[int, int], speed: int, image: str, angle: int, life_points: int, bullet: Tuple[Tuple[int, int], int, int, str]) -> None:
        super().__init__(size, position, speed, image, angle, life_points, bullet)


    def get_degree(self, x: int, y: int) -> int:
        # Calculate the angle in radians
        angle_rad = math.atan2(y, x)
        
        # Convert radians to degrees
        angle_deg = math.degrees(angle_rad)
        
        # Ensure the degree is positive
        if angle_deg < 0:
            angle_deg += 360
        
        return (angle_deg - 90) % 360

    def rotate(self, player: Player) -> None:

        x_enemy, y_enemy = self.position
        x_player, y_player = player.position

        x_offset = x_player - x_enemy
        y_offset = y_player - y_enemy

        self.angle = self.get_degree(x_offset, y_offset)

        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, player) -> None:
        self.rotate(player)

        x, y = self.position
        x_off, y_off = player.position
        x_diff, y_diff = (x - x_off), (y - y_off)
        self.rect.center = (400 + x_diff, 300 - y_diff)
        self.distance_from_player = math.sqrt(x_diff**2 + y_diff**2)
        self.move()
