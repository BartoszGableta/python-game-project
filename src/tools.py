import pygame


class EnemyGenerator:

    def __init__(self, limit, player, min_distance, max_distance, window):
        self.enemies = pygame.sprite.Group()
        self.limit = limit
        self.player = player
        self.window = window
        
    def change_limit(self, limit):
        self.limit = limit

    def generate_enemy(self, number_of_enemies):
        pass

    def recycle_enemies(self):
        pass

    def run(self):
        self.recycle_enemies()
        self.enemies.draw(self.window)
        self.enemies.update()
