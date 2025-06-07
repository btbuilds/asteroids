import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # dt = delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers =       (asteroids, updatable, drawable)
    AsteroidField.containers =  (updatable)
    Player.containers =         (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # sets player position to center of screen
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for x in asteroids:
            if x.collision_check(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for x in drawable:
            x.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # caps FPS to 60

if __name__ == "__main__":
    main()