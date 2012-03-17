import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xdif = x1 - x2;
    ydif = y1 - y2;
    return math.sqrt(xdif * xdif + ydif * ydif)

def distances(p, pts):
    result = []
    for pt in pts:
        result.append(distance(p, pt))
    return result
