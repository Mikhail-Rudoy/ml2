import random

def genoint():
    return [random.randrange(0, 200), random.randrange(0, 200)]

def genpoints(n):
    p = []
    for i in range(n):
        p.append(genpoint())
    return p

def splitpoints(points):
    xs, ys = [], []
    for pt in points:
        x,y = pt
        xs.append(x)
        ys.append(y)
    return [xs, ys]

def increment_word_tally(word, tally):
    wds = splitpoints(tally)[0]
    if word in wds:
         for i in range(len(wds)):
             if wds[i] == word:
                 tally[i][1] = tally[i][1] + 1
    else:
         tally.append([word,1])
    return tally
