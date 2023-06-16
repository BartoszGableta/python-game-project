from abc import ABC
from typing import Tuple
import pygame
import math


class Player(pygame.sprite.Sprite):
    
    def __init__(self, size, position, speed, image):
        super().__init__()

        image = pygame.image.load(image).convert_alpha()
        self.orig_image = pygame.transform.scale(image, size)
        self.image = self.orig_image

        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        
        self.position = position
        self.speed = speed
        self.angle = 0

    def move(self):
        x_change = self.speed * math.sin(math.radians(self.angle))
        y_change = self.speed * math.cos(math.radians(self.angle))
        self.position = (self.position[0] - x_change, self.position[1] + y_change)
        #print('player pos', self.position)

    def rotate_left(self, rotation):
        self.angle =  (self.angle + rotation) % 360

    def rotate_right(self, rotation):
        self.angle = (self.angle - rotation) % 360

    def update(self):
        self.move()
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, size, position, speed, image):
        super().__init__()

        image = pygame.image.load(image).convert_alpha()
        self.orig_image = pygame.transform.scale(image, size)
        self.image = self.orig_image

        self.rect = self.image.get_rect()
        self.rect.center = (200, 300)
        
        self.position = position
        self.speed = speed
        self.angle = 0

    def move(self) -> None:

        x_change = self.speed * math.sin(math.radians(self.angle))
        y_change = self.speed * math.cos(math.radians(self.angle))

        self.position = (self.position[0] - x_change, self.position[1] + y_change)

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

    def update(self, player):
        self.rotate(player)

        x, y = self.position
        x_off, y_off = player.position
        self.rect.center = (400 + (x - x_off), 300 - (y - y_off))
        self.move()
