import random

def build_mongrams(slist):
    d={}
    for word in slist:
        if d.has_key(word):
            d[word] = d[word] + 1
        else:
            d[word] = 1
    return d

def build_bigrams(slist):
    d={}
    for i in range(len(slist) - 1):
        prefix = slist[i]
        suffix = slist[i+1]
        if d.has_key(prefix):
            d[prefix].append(suffix)
        else:
            d[prefix] = [suffix]
    return d

def build_trigrams(slist):
    d={}
    for i in range(len(slist) - 2):
        prefix = " ".join(slist[i:i+2])
        suffix = slist[i+2]
        if d.has_key(prefix):
            d[prefix].append(suffix)
        else:
            d[prefix] = [suffix]
    return d


def build_ngrams(slist, n):
    d={}
    for i in range(len(slist) + 1 - n):
        prefix = " ".join(slist[i:i+n-1])
        suffix = slist[i+n-1]
        if d.has_key(prefix):
            d[prefix].append(suffix)
        else:
            d[prefix] = [suffix]
    return d

def load_file(filename):
    f = open(filename,"r")
    l = f.readlines()
    l2 = []
    for line in l:
        line = line.strip()
        line = line.lower()
        line2 = ""
        for i in range(len(line)):
            if line[i] in "abcdefghijklmnopqrstuvwxyz" or (line[i] == " " and line[i+1] != " "):
                line2=line2+line[i]
        if line2 != "":
            l2.append(line2)
    return " ".join(l2)

def make_sentence1(slist, length):
    s = ""
    for i in range(length):
        s = s + random.choice(slist) + " "
    print s

def make_sentence2(bigrams,length):
    allwords = bigrams.keys()
    s = random.choice(allwords)
    nextword = s
    for i in range(length):
        nextword = random.choice(bigrams[nextword])
        s = s + " " + nextword
    print s

def make_sentence3(trigrams,length):
    lastpairs = trigrams.keys()
    lastpair = random.choice(lastpairs)
    s = lastpair
    for i in range(length):
        nextword = random.choice(trigrams[lastpair])
        lastpair = lastpair[lastpair.find(" ") + 1 : ] + " " + nextword
        s = s + " " + nextword
    print s

def make_sentencen(slist, n, length):
    if n <= 1:
        make_sentence1(slist, length)
        return
    if n == 2:
        make_sentence2(build_bigrams(slist), length)
        return
    if n == 3:
        make_sentence3(build_trigrams(slist), length)
        return
    ngrams = build_ngrams(slist, n)
    lastnmos = ngrams.keys()
    lastnmo = random.choice(lastnmos)
    s = lastnmo
    for i in range(length):
        nextword = random.choice(ngrams[lastnmo])
        lastnmo = lastnmo[lastnmo.find(" ") + 1 : ] + " " + nextword
        s = s + " " + nextword
    print s

text = load_file("psalms.txt").split() + load_file("moby_dick.txt").split() + load_file("sonnets.txt").split()

for i in range(1, 7):
    make_sentencen(text, i, 40)
    print ""
