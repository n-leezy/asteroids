from circleshape import CircleShape
from constants import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width=2) # draws the circle

    def update(self, dt):
        self.position += (self.velocity * dt) # move in a straight line at a constant speed

