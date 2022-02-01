import math

import pygame
from Classes.Movable import Movable
from src.helper import clamp, deg_to_rad, rotate_vector

class Lawnmower(Movable):
    def __init__(self,x,y):
        self.scale = .3
        width = 25
        height=100
        super().__init__(x,y,width,height,(0,height*.3),270)
        self.original_image = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load("./Images/lawnmower_0.png"), 180),
            (self.hitbox.width, self.hitbox.height),
        )
        self.image = self.original_image
        self.radius = self.width / 2



    def draw(self, win):
        angle = self.angle - 270

        #win.blit(self.image, (self.x-self.width/2, self.y-self.height/2))
        #pygame.draw.line(win,(0,0,0),(self.width/2+self.x,self.height/2+self.y),(self.width/2+self.x+self.center_to_pivot_vector[0],self.height/2+self.y+self.center_to_pivot_vector[1]),4)
        #pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.width,self.height),2)
        pygame.draw.circle(win,(255,0,0),(self.x,self.y),3)
        self.hitbox.draw(win)

    def cut(self, grass):
        square = grass.get_square((self.x, self.y))

        min_box = grass.get_square((self.x - self.radius, self.y - self.radius))
        max_box = grass.get_square((self.x + self.radius, self.y + self.radius))
        min_box[0] = clamp(min_box[0], 0, grass.resolution)
        min_box[1] = clamp(min_box[1], 0, grass.resolution)
        max_box[0] = clamp(max_box[0], 0, grass.resolution)
        max_box[1] = clamp(max_box[1], 0, grass.resolution)

        for i in range(min_box[0], max_box[0]):
            for j in range(min_box[1], max_box[1]):
                box_center = grass.box_centers[i][j]
                if (box_center[0] - self.x) ** 2 + (
                    box_center[1] - self.y
                ) ** 2 < self.radius ** 2:
                    grass.cut(i, j)

    def update(self):
        super().update()
        self.image = pygame.transform.rotate(self.original_image, -self.angle - 90)

