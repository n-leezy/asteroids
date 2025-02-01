from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width=2) # draws the circle

    def update(self, dt):
        self.position += (self.velocity * dt) # move in a straight line at a constant speed

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        positive_velocity = self.velocity.rotate(random_angle)
        negative_velocity = self.velocity.rotate(random_angle*-1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_one = Asteroid(self.position.x,self.position.y, new_radius)
        split_asteroid_two = Asteroid(self.position.x ,self.position.y, new_radius)
        split_asteroid_one.velocity = positive_velocity * 1.2
        split_asteroid_two.velocity = negative_velocity * 1.2
        for group in self.groups(): # must add split asteroids to groups to be able to update and render them correctly
            group.add(split_asteroid_one)
            group.add(split_asteroid_two)