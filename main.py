import pygame

from constants import BLACK, FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE
from classes.player import Player
from classes.enemy import Enemy
from utils.collision import check_collision


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()

    player = Player(100, 100)
    enemy = Enemy(500, 300)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        enemy.update()

        if check_collision(player, enemy):
            print("Collision detected!")

        screen.fill(BLACK)

        player.draw(screen)
        enemy.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
