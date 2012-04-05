import math
import random

def dist(A, B):
    sumofsqrs = 0
    for i in range(len(A)):
        sumofsqrs = sumofsqrs + (A[i] - B[i]) * (A[i] - B[i])
    return math.sqrt(sumofsqrs)

def make_points(n):
    l=[]
    for i in range(n):
        l.append([random.randrange(0, 301), random.randrange(0, 301)])
    return l

def make_centroids(n, pointlist):
    return random.sample(pointlist, n)

def closest(pt, pointlist):
    bestindex = 0
    bestdistance = dist(pt, pointlist[0])
    for i in range(len(pointlist)):
        d = dist(pt, pointlist[i])
        if d < bestdistance:
            bestdistance = d
            bestindex = i
    return bestindex

def make_cluster(centroids, pointlist):
    cs = []
    for i in centroids:
        cs.append([])
    for pt in pointlist:
        cs[closest(pt, centroids)].append(pt)
    return cs
