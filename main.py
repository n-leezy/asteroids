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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets the screen to be used
    clock = pygame.time.Clock() # instantiates the clock variable

    x = SCREEN_WIDTH / 2 # finds the midpoint of the screen
    y = SCREEN_HEIGHT / 2
    player = Player(x, y) # instantiate player class

    updateables = pygame.sprite.Group(player) # group the updateable sprites together
    drawables = pygame.sprite.Group(player) # group the drawable sprites together

    dt = 0

    # beginning of the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quits the program if the exit button is pressed
                pygame.quit()
                return
        pygame.Surface.fill(screen, BLACK) # fills the game screen with black
        for updateable in updateables: # updates the updateables
            updateable.update(dt)
        for drawable in drawables: # draws the drawables
            drawable.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) # Pauses the game loop until 1/nth of a second has passed, returns the amount of time passed since last called
        dt = delta_time / 1000 # stores the delta time in seconds into dt

if __name__ == "__main__":
    main()
    pygame.quit()

