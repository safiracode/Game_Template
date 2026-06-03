import pygame
from classes.game_object import GameObject

from constants import COIN_HEIGHT, COIN_WIDTH, YELLOW

class Coin(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, COIN_WIDTH, COIN_HEIGHT, YELLOW)
    
    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
