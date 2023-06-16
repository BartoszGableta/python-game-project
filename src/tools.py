import pygame
import math
import random
from src.characters import Enemy


class EnemyGenerator:

    def __init__(self, limit, player, generation_distance, max_distance, window):
        self.enemies = pygame.sprite.Group()
        self.limit = limit
        self.player = player
        self.window = window
        self.max_distance = max_distance
        self.generation_distance = generation_distance
        
    def change_limit(self, limit):
        self.limit = limit

    def calculate_y(self, x):
        y_squared = (self.generation_distance ** 2) - (x ** 2)
        #print(self.generation_distance, x)
        y1 = - (y_squared ** .5) // 1
        y2 = (y_squared ** .5) // 1

        return random.choice([y1, y2])


    def generate_enemy(self):
        player_x, player_y = self.player.position
        player_x, player_y = int(player_x), int(player_y)
        
        if len(self.enemies) < self.limit:
            x = random.randint(-self.generation_distance, self.generation_distance)
            y = self.calculate_y(x)

            self.enemies.add(Enemy((50, 50), (player_x + x, player_y + y), 2, "assets/enemy.png"))

    def recycle_enemies(self):
        for enemy in self.enemies:
            if math.dist(enemy.position, self.player.position) > self.max_distance:
                #print('removed')
                enemy.kill()

    def run(self):
        self.recycle_enemies()
        self.enemies.update(self.player)
        self.enemies.draw(self.window)
