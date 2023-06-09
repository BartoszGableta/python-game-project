from abc import ABC
import pygame

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
        self.movement = (False, False, False, False)
        self.scale()

    def move(self):
        """
        The function moves the ship controlled by the player,
        simulating the movement of the spaceship
        x: int,
        y: int
        """
        move_left, move_up, move_right, move_down = self.movement
        x_change = 0
        y_change = 0
        if move_left:
            x_change = -self.speed
        if move_right:
            x_change = self.speed
        if move_up:
            y_change = -self.speed
        if move_down:
            y_change = self.speed
        
        self.position = tuple(map(lambda i, j: i + j, (x_change, y_change), self.position))
        print(self.position)

    def scale(self):
        players_spaceship = pygame.transform.scale(self.image, self.size)

class Player(Character):
    pass
