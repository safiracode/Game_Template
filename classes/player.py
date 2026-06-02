import pygame

from constants import BLUE, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from classes.game_object import GameObject
from utils.helpers import clamp


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT, BLUE)
        self.speed = PLAYER_SPEED

    def handle_movement(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.x = clamp(self.x, 0, SCREEN_WIDTH - self.width)
        self.y = clamp(self.y, 0, SCREEN_HEIGHT - self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
