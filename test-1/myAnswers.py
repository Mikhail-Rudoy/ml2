def howCold(deg):
    if deg < 45:
        return "Cold"
    elif deg <= 75:
        return "Moderate"
    else:
        return "Warm"

def ticket(speed, birthday):
    if birthday:
        extra = 5
    else:
        extra = 0
    if speed <= 60 + extra:
        return 0
    if speed <= 80 + extra:
        return 1
    else:
        return 2

def howManyThrees(l):
    num = 0
    for n in l:
        if n == 3:
            num = num + 1
    return num

def flipCase(s):
    result = ""
    for c in s:
        if c == c.upper():
            result = result + c.lower()
        else:
            result = result + c.upper()
    return result

def findsecond(word, s):
    return s[s.find(word) + 1:].find(word) + s.find(word) + 1

def sumwithout13(l):
    sum = 0
    for n in l:
        if n != 13:
            sum = sum + n
    return sum

def remove13(l):
    result = []
    for n in l:
        if n != 13:
            result = result + [n]
    return result
