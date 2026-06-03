import pygame

from constants import BLUE, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from classes.game_object import GameObject
from utils.collision import check_collision
from utils.helpers import clamp


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT, BLUE)
        self.speed = PLAYER_SPEED

    def handle_movement(self):

        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            dx -= self.speed

        if keys[pygame.K_RIGHT]:
            dx += self.speed

        if keys[pygame.K_UP]:
            dy -= self.speed

        if keys[pygame.K_DOWN]:
            dy += self.speed

        self.x = clamp(self.x + dx, 0, SCREEN_WIDTH - self.width)
        self.y = clamp(self.y + dy, 0, SCREEN_HEIGHT - self.height)



    def coin_collisions(self, coins, coin_counter):
        for coin in coins[:]:
            if check_collision(self, coin):
                coin_counter += 1
                coins.remove(coin)
        
        return coin_counter


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())

    
    def update(self, screen, coins, coin_counter):

        self.handle_movement()
        self.draw(screen)
        coin_counter = self.coin_collisions(coins, coin_counter)

        return coin_counter

