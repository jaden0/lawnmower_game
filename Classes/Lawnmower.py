import math

import pygame
from Classes.Movable import Movable
from src.helper import clamp, deg_to_rad, rotate_vector

class Lawnmower(Movable):
    def __init__(self,x,y):
        self.scale = .3
        width = 40
        height=100
        super().__init__(x,y,width,height,(0,height*.3),270)
        #super().__init__(x,y,width,height,(10,height*1.3),270)
        self.original_image = []
        for i in range(0,2):
            self.original_image.append(pygame.transform.scale(
                pygame.transform.rotate(pygame.image.load("./Images/lawnmower_%d.png" % i), 180),
                (self.hitbox.width, self.hitbox.height),
            ))
        self.image_index = 0
        self.steps_per_image = 6
        self.image = self.original_image[0]
        self.image_tick = 0
        self.radius = self.width / 2
        self.rotated_p_vector = [self.hitbox.p_vector[0]-self.width/2, self.hitbox.p_vector[1]-self.height/2]
        self.rotated_p_vector = self.hitbox.p_vector


    def draw(self, win):
        angle = self.angle - 270

        win.blit(self.image, (self.x-self.image.get_width()/2+self.rotated_p_vector[0], self.y-self.image.get_height()/2+self.rotated_p_vector[1]))
        #pygame.draw.circle(win,(255,0,0),(self.x,self.y),3)
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
        theta = deg_to_rad(self.angle-270)
        new_x = math.cos(theta)*(self.hitbox.p_vector[0]) - math.sin(theta)*(self.hitbox.p_vector[1])
        new_y = math.sin(theta)*(self.hitbox.p_vector[0]) + math.cos(theta)*(self.hitbox.p_vector[1])
        self.rotated_p_vector = [new_x,new_y]
        self.image_tick += 1
        self.image_tick = self.image_tick % self.steps_per_image
        if self.image_tick == 0:
            self.image_index += 1
            self.image_index = self.image_index % (len(self.original_image))
        self.image = pygame.transform.rotate(self.original_image[self.image_index], -self.angle - 90)

