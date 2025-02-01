from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot


# Player class that inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.timer = 0

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

    # updates the player on the screen
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt 

        if keys[pygame.K_a]:
            self.rotate(dt*-1) # multiply by -1 for opposite rotation
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    # moves the ship back and forth with the w and s keys
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # controls the shots of the player
    def shoot(self, dt):
        if self.timer <= 0:
            current_shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            shot_direction = pygame.Vector2(0,1).rotate(self.rotation)
            current_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
            self.shots_group.add(current_shot)
            self.timer = 0.3
