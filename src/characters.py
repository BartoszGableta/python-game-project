from abc import ABC
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

    def __init__(self, size, position, speed, image_file) -> None:
        self.size = size
        self.position = position
        self.speed = speed
        self.image = pygame.image.load(image_file).convert_alpha()
        self.angle = 0
        self.direction_of_rotation = 0
        self.scale()

    def move(self):
        """
        The function moves the ship controlled by the player,
        simulating the movement of the spaceship
        """
        x_change = self.speed * math.sin(math.radians(self.angle))
        y_change = self.speed * math.cos(math.radians(self.angle))
        print(f"({x_change/self.speed},{y_change/self.speed})")
        print(f"Angle: {self.angle}")
        print(f"Position: {self.position}")
        self.position = tuple(map(lambda i, j: i + j, (-x_change, -y_change), self.position))

    def rotate(self, angle_change):
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
