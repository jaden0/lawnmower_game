import math
from Classes.Hitbox import Hitbox
from src.helper import deg_to_rad,rad_to_deg

class Movable(object):
    def __init__(self, x, y, width, height, p_vector, angle):
        self.step = 5
        self.anglestep = 5
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.hitbox = Hitbox(self.x,self.y,self.width,self.height,self.angle,p_vector)

    def update_hitbox(self,instruction):
        # 0: forward, 1: backbwards, 2: left, 3: right
        new_angle = self.angle
        new_position_x = self.x
        new_position_y = self.y
        if instruction in [0, 1]:
            if instruction == 0:  # forwards
                new_position_x = self.x + self.step * math.cos(deg_to_rad(self.angle))
                new_position_y = self.y + self.step * math.sin(deg_to_rad(self.angle))
            if instruction == 1:  # backwards
                new_position_x = self.x - self.step * math.cos(deg_to_rad(self.angle))
                new_position_y = self.y - self.step * math.sin(deg_to_rad(self.angle))
        if instruction == 2:  # left
            new_angle = self.angle - self.anglestep

        if instruction == 3:  # right
            new_angle = self.angle + self.anglestep
        self.hitbox.update(new_position_x, new_position_y, new_angle)

    def update(self):
        self.x = self.hitbox.x
        self.y = self.hitbox.y
        self.angle = self.hitbox.angle

    def reset(self):
        self.hitbox.update(self.x,self.y,self.angle)