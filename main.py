# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player

BLACK = (0,0,0)

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.Surface.fill(screen, BLACK)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        delta_time = clock.tick(60) # Pauses the game loop until 1/nth of a second has passed, returns the amount of time passed since last called
        dt = delta_time / 1000 # stores the delta time in seconds into dt

if __name__ == "__main__":
    main()
    pygame.quit()

