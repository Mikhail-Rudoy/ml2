#1)

def splitlist(l):
    xs, ys = [], []
    for item in l:
        xs = xs + [item[0]]
        ys = ys + [item[1]]
    return xs, ys

print splitlist([[2, 3], [10, 30], [42, 44]])

#2)

def combine(l1, l2):
    i = 0
    result = []
    while i < len(l1) and i < len(l2):
        result.append([l1[i], l2[i]])
        i = i + 1
    return result

print combine([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
print combine([1, 2, 3, 4, 5], [10, 20])

#3)

import math

def dist(A, B):
    sumofsqrs = 0
    for i in range(len(A)):
        sumofsqrs = sumofsqrs + (A[i] - B[i]) * (A[i] - B[i])
    return math.sqrt(sumofsqrs)

print dist([0, 0, 0, 0], range(4))

#4)

def closest(pt, pointlist):
    bestindex = 0
    bestdistance = dist(pt, pointlist[0])
    for i in range(len(pointlist)):
        d = dist(pt, pointlist[i])
        if d < bestdistance:
            bestdistance = d
            bestindex = i
    return bestindex

print closest([0, 0, 0], [[3, 4, 5], [2, 1, 4], [1, 4, 1], [-2, 3, 2]])
