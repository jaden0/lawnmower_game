import math

import pygame


def clamp(i, min_val, max_val):
    o = i
    if o > max_val:
        o = max_val
    if o < min_val:
        o = min_val
    return o


def deg_to_rad(degrees):
    return degrees * math.pi / 180


def rad_to_deg(radians):
    return (radians * 180 / math.pi) % 360

def point_on_line(p1,p2,x):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    y = (y2-y1)/(x2-x1+.00001)*(x-x2)+y2
    return( y )

def is_between(limit_1, limit_2, point):
    if point >= min( limit_1, limit_2) and point <= max( limit_1, limit_2):
        return( True )
    else:
        return( False )

def rotate_vector(v,angle):
    theta = deg_to_rad(angle)
    x_prime = math.cos(theta)*v[0] - math.sin(theta)*v[1]
    y_prime = math.sin(theta)*v[0] + math.cos(theta)*v[1]
    return( [x_prime,y_prime])

def dot(a,b):
    return( a[0]*b[0]+a[1]*b[1])

def mag(a):
    return( math.sqrt(a[0]**2 + a[1]**2 ) )

def get_vector_from_line_to_point(line,point):
    a = [line[1][0] - line[0][0],line[1][1] - line[0][1]]
    b = [point[0]-line[0][0],point[1]-line[0][1]]
    scaler = dot(a,b)/(mag(a)**2)
    output = [b[0]-a[0]*scaler,b[1]-a[1]*scaler]
    return( output )


