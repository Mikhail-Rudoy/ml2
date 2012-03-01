def stringTimes(s,n):
    return n * s
def countFives(l):
    num = 0
    for n in l:
        if n == 5:
            num = num + 1
    return num
def listSum(l):
    sum = 0
    for n in l:
        sum = sum + n
    return sum
def numtimes(word, sentence):
    return len(sentence.split(word)) - 1
def countOdds(l):
    num = 0
    for n in 1:
        num = num + (n % 2)
    return num
def capWords(sentence):
    l = sentence.split(" ")
    for i in range(len(l)):
        l[i] = l[i][0].upper() + l[i][1:]
    return " ".join(l)
def expand(s):
    soFar = ""
    for i in range(len(s)):
        soFar = soFar + (i + 1) * s[i]
    return soFar

print "stringTimes('hi', 4) =", stringTimes('hi', 4)
print "countFives([5, 3, 2, 4, 2, 5, 2, 4, 5, 6, 7]) =", countFives([5, 3, 2, 4, 2, 5, 2, 4, 5, 6, 7])
print "listSum([5, 2, 3]) =", listSum([5, 2, 3])
print "numtimes('the', 'it is the time of the season') =", numtimes('the', 'it is the time of the season')
#print "countOdds([1, 2, 3, 4, 5]) =", countOdds([1, 2, 3, 4, 5])
print "capWords('hi im mike') =", capWords('hi im mike')
print "expand('abcde') =", expand('abcde')
