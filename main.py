from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
import pygame


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        # Inside your main loop
        dt = clock.tick(60) / 1000
        actual_fps = 1 / dt if dt > 0 else 0
        print(f"Current FPS: {actual_fps:.2f}")


if __name__ == "__main__":
    main()
