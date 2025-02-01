# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets the screen to be used
    clock = pygame.time.Clock() # instantiates the clock variable

    x = SCREEN_WIDTH / 2 # finds the midpoint of the screen
    y = SCREEN_HEIGHT / 2
    

    updateables = pygame.sprite.Group() # group the updateable sprites together
    drawables = pygame.sprite.Group() # group the drawable sprites together
    asteroids = pygame.sprite.Group() # group to contain all the asteroids
    shots = pygame.sprite.Group() # group to contain player's shots

    Player.containers = (updateables, drawables) # adds player to both groups
    Asteroid.containers = (asteroids, updateables, drawables) # adds asteroid to groups
    AsteroidField.containers = (updateables) # asteroidfield group set
    Shot.containers = (drawables, updateables)

    
    player = Player(x, y, shots) # instantiate player class
    asteroid_field = AsteroidField() # instantiate asteroid field

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
        for asteroid in asteroids: # collision check with player
            if asteroid.collisions(player):
                print("Game over!")
                pygame.quit()
                return
        for asteroid in asteroids: # collision check for shots and asteroids
            for bullet in shots:
                if asteroid.collisions(bullet):
                    asteroid.split()
                    bullet.kill()
        delta_time = clock.tick(60) # Pauses the game loop until 1/nth of a second has passed, returns the amount of time passed since last called
        dt = delta_time / 1000 # stores the delta time in seconds into dt

if __name__ == "__main__":
    main()
    pygame.quit()

