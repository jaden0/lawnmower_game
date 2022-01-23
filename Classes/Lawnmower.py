import pygame.image
import math
from src.helper import clamp

class Lawnmower(object):
    def __init__(self, x, y):
        self.step = 5
        self.anglestep = 2
        self.x = x
        self.y = y
        self.angle = 270
        self.scale = .4
        self.width = 1000
        self.height = 1000
        self.radius = self.width*self.scale*.06
        self.original_image = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("./Images/lawnmower.png"),180),(self.scale*self.width,self.scale*self.height))
        self.image = self.original_image

    def deg_to_rad(self, degrees):
        return degrees * math.pi / 180

    def rad_to_deg(self, radians):
        return (radians * 180 / math.pi) % 360


    def draw(self, win):
        x_shift = -self.image.get_width()/2
        y_shift = -self.image.get_height()/2
        win.blit(self.image, (self.x+x_shift,self.y+y_shift))

        #pygame.draw.circle(win,(255,0,0),(self.x,self.y),5)

    def move(self, instruction):
        # 0: forward, 1: backbwards, 2: left, 3: right
        if instruction in [0,1]:
            if instruction == 0: # forwards
                new_position_x = self.x + self.step * math.cos(
                    self.deg_to_rad(self.angle)
                )
                new_position_y = self.y + self.step * math.sin(
                    self.deg_to_rad(self.angle)
                )
            if instruction == 1: # backwards
                new_position_x = self.x - self.step * math.cos(
                    self.deg_to_rad(self.angle)
                )
                new_position_y = self.y - self.step * math.sin(
                    self.deg_to_rad(self.angle)
                )
            self.x = new_position_x
            self.y = new_position_y
        if instruction == 2: # left
            self.angle -= self.anglestep
            self.image = pygame.transform.rotate(self.original_image, -self.angle-90)
        if instruction == 3: # right
            self.angle += self.anglestep
            self.image = pygame.transform.rotate(self.original_image, -self.angle-90)

    def cut(self,grass):
        square = grass.get_square((self.x,self.y))


        min_box = grass.get_square((self.x-self.radius, self.y - self.radius))
        max_box = grass.get_square((self.x+self.radius, self.y + self.radius))
        min_box[0] = clamp(min_box[0],0,grass.resolution)
        min_box[1] = clamp(min_box[1],0,grass.resolution)
        max_box[0] = clamp(max_box[0],0,grass.resolution)
        max_box[1] = clamp(max_box[1],0,grass.resolution)

        for i in range(min_box[0], max_box[0]):
            for j in range( min_box[1], max_box[1]):
                box_center = grass.box_centers[i][j]
                if (box_center[0]-self.x)**2 + (box_center[1]-self.y)**2 < self.radius**2:
                    grass.cut(i,j)


