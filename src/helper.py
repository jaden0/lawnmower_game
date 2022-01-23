def clamp( i, min, max):
    o = i
    if o > max:
        o = max
    if o < min:
        o = min
    return( o )
