import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # dt = delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # sets player position to center of screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # caps FPS to 60

if __name__ == "__main__":
    main()