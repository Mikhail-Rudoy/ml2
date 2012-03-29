import random

def add_word(d,word):
    if d.has_key(word):
        d[word] = d[word] + 1
    else:
        d[word]=1
    return d

def build_bigrams(slist):
    d={}
    # [the,try,works,are,planted,in,the,something]
    for i in range(len(slist)-1):
        prefix = slist[i]
        suffix = slist[i+1]
        if d.has_key(prefix):
            # it's already in the dictionary
            d[prefix].append(suffix)
        else:
            # it isn't in the dictionary yet
            #nl = []
            #nl.append(suffix)
            #d[prefix] = nl
            d[prefix] = [suffix]
    return d


def build_word_freq(slist):
    d={}
    for word in slist:
        d = add_word(d,word)
    return d



def load_file(filename):
    f = open(filename,"r")
    l = f.readlines()
    l2 = []
    for line in l:
        line = line.strip()
        line = line.lower()
        line2 = ""
        for c in line:
            if c in "abcdefghijklmnopqrstuvwxyz ":
                line2=line2+c
        l2.append(line2)
    return " ".join(l2)

def make_sentence(bigrams,length):
    allwords = bigrams.keys()
    
    nextword= random.choice(allwords)
    s=nextword
                            
    for i in range(length):
        nextword= random.choice(bigrams[nextword])
        s = s + " " + nextword
    print s
    
text = load_file("psalms.txt")

#print text
#freq= build_word_freq(text.split())
bigrams = build_bigrams(text.split())
print "Done"
make_sentence(bigrams,50)
#print bigrams
#l=build_word_freq("I will not eat them sam I am I will not eat green eggs and ham")
#print l
#l = build_word_freq("fred waldo barney")
#print l
#l = build_word_freq("I will not eat them sam I am I will not eat green eggs and ham".split())
#print l

