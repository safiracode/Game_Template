import pygame

from constants import ENEMY_HEIGHT, ENEMY_SPEED, ENEMY_WIDTH, RED, SCREEN_WIDTH
from classes.game_object import GameObject


class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_WIDTH, ENEMY_HEIGHT, RED)
        self.speed = ENEMY_SPEED

    def update(self):
        self.x += self.speed

        if self.x > SCREEN_WIDTH:
            self.x = -self.width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
