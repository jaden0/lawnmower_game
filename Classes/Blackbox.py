import pygame
from Classes.Movable import Movable
class Blackbox(Movable):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height,(0,0),270)


    def draw(self,win):
        pygame.draw.rect(win,(0,0,255),(self.x-self.width/2,self.y-self.height/2,self.width,self.height))
        self.hitbox.draw(win)

