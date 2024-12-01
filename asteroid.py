import pygame
from circleshape import *
from constants import *
import random 


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self,dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        split_angle=random.uniform(20,50)
        pos_v=self.velocity.rotate(split_angle)
        neg_v=self.velocity.rotate(-split_angle)
        new_rad=self.radius-ASTEROID_MIN_RADIUS
        asteroid=Asteroid(self.position.x,self.position.y,new_rad)
        asteroid.velocity=pos_v*2
        asteroid=Asteroid(self.position.x,self.position.y,new_rad)
        asteroid.velocity=neg_v*2



    
    

