# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    pygame.init()
    window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        clock=pygame.time.Clock()
        dt=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(window, (0,0,0))
        pygame.display.flip()
        dt=clock.tick(60)/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")











if __name__=="__main__":
    main()