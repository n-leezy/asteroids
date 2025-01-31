from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape
import pygame

WHITE = (255, 255, 255)

# Player class that inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class, draws the player as a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # draws a white "player" to the middle of the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    # controls rotation of the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1) # multiply by -1 for opposite rotation
        if keys[pygame.K_d]:
            self.rotate(dt)

