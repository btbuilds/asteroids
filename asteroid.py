import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20, 50)
        ast_one_velocity = self.velocity.rotate(spawn_angle)
        ast_two_velocity = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_one = Asteroid(self.position.x, self.position.y, new_radius)
        ast_one.velocity = ast_one_velocity * 1.2
        ast_two = Asteroid(self.position.x, self.position.y, new_radius)
        ast_two.velocity = ast_two_velocity * 1.2