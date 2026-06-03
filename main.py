import pygame

from constants import BLACK, FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE
from classes.player import Player
from classes.enemy import Enemy
from classes.coin import Coin
from classes.text import Text
from utils.collision import check_collision


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()

    player = Player(100, 100)
    enemy = Enemy(500, 300)

    coin_counter = 0

    coins = [
        Coin(400, 150),
        Coin(400, 250),
        Coin(400, 350)
    ]

    coins_display = Text(25, 25)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy.update()

        if check_collision(player, enemy):
            print("Collision detected!")

        screen.fill(BLACK)

        for coin in coins:
            coin.update(screen)

        coin_counter = player.update(screen, coins, coin_counter)
        enemy.draw(screen)

        coins_display.display(screen, f"Moedas: {coin_counter}")

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
