# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Player.containers=(updatable,drawable)
    Shot.containers=(shots,updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable) 
    AsteroidField.containers=updatable

    asteroid_field=AsteroidField()  
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt=0
       
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(window, (0,0,0))
        for object in updatable:
            object.update(dt)
            for ast in asteroids:
                if player.collision(ast):
                    sys.exit("Game over!")
                for shot in shots:
                    if ast.collision(shot):
                        shot.kill()
                        ast.split()
        for object in drawable:
            object.draw(window)
        pygame.display.flip()
        dt=clock.tick(60)/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    










if __name__=="__main__":
    main()