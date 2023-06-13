from abc import ABC
from typing import Tuple
import pygame
import math

class Character(ABC):
    """
    Class represents unidentified figure, e.g. of a player or an opponent
    size: Tuple[int, int],
    position: Tuple[int, int],
    speed: float,
    image: str
    """

    def __init__(self, size: Tuple[int, int], position: Tuple[int, int], speed: float, image_file: str) -> None:
        self.size = size
        self.position = position
        self.speed = speed
        self.image = pygame.image.load(image_file).convert_alpha()
        self.angle = 0
        self.direction_of_rotation = 0

    def move(self) -> None:
        """
        The function moves the ship controlled by the player,
        simulating the movement of the spaceship
        """
        x_change = self.speed * math.sin(math.radians(self.angle))
        y_change = self.speed * math.cos(math.radians(self.angle))
        print(f"({x_change/self.speed},{y_change/self.speed})")
        print(f"Angle: {self.angle}")
        print(f"Position: {self.position}")
        self.position = tuple(map(lambda i, j: i + j, (-x_change, y_change), self.position))

    def rotate(self, angle_change: float) -> None:
        """
        The function rotates the vessel
        by a given angle expressed in degrees
        """
        if self.direction_of_rotation > 0:
            if self.direction_of_rotation == 1:
                self.angle += angle_change
            else:
                self.angle -= angle_change

        while self.angle > 359:
            self.angle -= 360

        while self.angle < 0:
            self.angle += 360


class Player(Character):
    pass

class Enemy(Character):

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
        """
        This function sets the enemy rotation to be suited for player position.
        """

        x_enemy, y_enemy = self.position
        x_player, y_player = player.position


        print("Enemy pos:", (x_enemy, y_enemy))

        x_offset = x_player - x_enemy
        y_offset = y_player - y_enemy

        print(self.get_degree(x_offset, y_offset))

        self.angle = self.get_degree(x_offset, y_offset)


