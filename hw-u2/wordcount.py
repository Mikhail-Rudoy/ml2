def tally_list(l):
    ht = {}
    for word in l:
        if ht.has_key(word):
            ht[word] = ht[word] + 1
        else:
            ht[word] = 1
    return ht

def tally_line(ln):
    return tally_list(ln.strip().split(" "))
    
def tally_file(f):
    lines = open(f, "r").readlines()
    result = []
    for l in lines:
        result.append(l.strip())
    return tally_line(" ".join(result))

def next_tally_list(l):
    ht = {}
    for i in range(len(l) - 1):
        if ht.has_key(l[i]):
            ht[l[i]] = ht[l[i]] + [l[i+1]]
        else:
            ht[l[i]] = [l[i+1]]
    if not ht.has_key(l[-1]):
        ht[l[-1]] = []
    return ht

def next_tally_line(ln):
    return next_tally_list(ln.strip().split(" "))
    
def next_tally_file(f):
    lines = open(f, "r").readlines()
    result = []
    for l in lines:
        result.append(l.strip())
    return next_tally_line(" ".join(result))
