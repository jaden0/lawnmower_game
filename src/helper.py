import math

def clamp( i, min, max):
    o = i
    if o > max:
        o = max
    if o < min:
        o = min
    return( o )

def deg_to_rad(degrees):
    return degrees * math.pi / 180

def rad_to_deg(radians):
    return (radians * 180 / math.pi) % 360
