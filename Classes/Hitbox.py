import pygame
import math
from src.helper import deg_to_rad, point_on_line, is_between, rotate_vector, get_vector_from_line_to_point, dot,mag
class Hitbox(object):
    def __init__(self,x,y,width, height, angle=0,p_vector=(0,0)):
        self.x = x
        self.y = y
        self.width= width
        self.height= height
        self.angle = angle
        self.p_vector = p_vector # vector from pivot to center
        self.update(x,y,angle)

    def _rotate(self,x,y,x_pivot,y_pivot,theta):
        x_prime = math.cos(theta)*(x-self.x) - math.sin(theta)*(y-self.y)
        y_prime = math.sin(theta)*(x-self.x) + math.cos(theta)*(y-self.y)
        return( [x_prime+self.x,y_prime+self.y])


    def update(self,x,y,angle):
        self.x=x
        self.y=y
        self.angle=angle
        self.corners = [[self.p_vector[0]-self.width/2,self.p_vector[1]-self.height/2],[self.p_vector[0]+self.width/2,self.p_vector[1]-self.height/2],
                        [self.p_vector[0]+self.width/2,self.p_vector[1]+self.height/2],[self.p_vector[0]-self.width/2,self.p_vector[1]+self.height/2]]
        for i in range(0,4):
            self.corners[i] = rotate_vector(self.corners[i],self.angle-270)
            self.corners[i] = [self.corners[i][0]+self.x,self.corners[i][1]+self.y]



    def draw(self,win):
        pygame.draw.lines(win,(0,0,0),True,self.corners,1)

    def is_hit(self,p):
        x = p[0]
        y = p[1]
        hit = True
        point_vector = get_vector_from_line_to_point([self.corners[0],self.corners[1]],[x,y])
        other_line_vector = get_vector_from_line_to_point([self.corners[0],self.corners[1]],self.corners[2])
        if dot(point_vector,other_line_vector) < 0 or mag(point_vector) > mag( other_line_vector):
            hit = False
        point_vector = get_vector_from_line_to_point([self.corners[1],self.corners[2]],[x,y])
        other_line_vector = get_vector_from_line_to_point([self.corners[1],self.corners[2]],self.corners[3])
        if dot(point_vector,other_line_vector) < 0 or mag(point_vector) > mag( other_line_vector):
            hit = False
        return( hit )


