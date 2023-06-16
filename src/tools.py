import pygame
import math
import random
from src.entities import Enemy, Player


class EnemyGenerator:
    """
    Class for generating and maintaining Enemies
    """

    def __init__(self, limit: int, player: Player, generation_distance: int, max_distance: int, window: pygame.surface) -> None:
        self.limit = limit
        self.player = player
        self.generation_distance = generation_distance
        self.max_distance = max_distance
        self.window = window

        self.enemies = pygame.sprite.Group()
        
    def change_limit(self, limit: int) -> None:
        """
        Method for changing the limit of enemies
        """
        self.limit = limit

    def calculate_y(self, x: int) -> int:
        """
        Method for calculating y for given x so it satisfies the generation distance
        """
        y_squared = (self.generation_distance ** 2) - (x ** 2)
        y1 = - (y_squared ** .5) // 1
        y2 = (y_squared ** .5) // 1

        return random.choice([y1, y2])

    def generate_enemy(self, size: int, speed: float, image: str) -> None:
        """
        Method for generating an enemy
        """
        print(len(self.enemies))
        player_x, player_y = self.player.position
        player_x, player_y = int(player_x), int(player_y)
        
        if len(self.enemies) < self.limit:
            x = random.randint(-self.generation_distance, self.generation_distance)
            y = self.calculate_y(x)

            position = (player_x + x, player_y + y)

            self.enemies.add(Enemy(size, position, speed, image))

    def recycle_enemies(self) -> None:
        """
        Method for recycling enemies that are further than max distance
        """
        for enemy in self.enemies:
            if math.dist(enemy.position, self.player.position) > self.max_distance:
                enemy.kill()

    def run(self) -> None:
        """
        Method for running all other methods that maintain enemies along the game
        """
        self.recycle_enemies()
        self.enemies.update(self.player)
        self.enemies.draw(self.window)
