import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # dt = delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers =       (updatable, drawable, asteroids)
    AsteroidField.containers =  (updatable)
    Player.containers =         (updatable, drawable)
    Shot.containers =           (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # sets player position to center of screen
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        # check if player hits an asteroid
        for x in asteroids:
            if x.collision_check(player):
                print("Game over!")
                sys.exit()

        # check if shots hit asteroids
        for x in asteroids: 
            for y in shots:
                if x.collision_check(y):
                    x.split()
                    y.kill()

        screen.fill("black")

        for x in drawable:
            x.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # caps FPS to 60

if __name__ == "__main__":
    main()