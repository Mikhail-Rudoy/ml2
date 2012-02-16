def capitalize(name):
    """
    capitalizes a lowercase name
    """
    i = name.find(" ") + 1
    if i == 0:
        return name[0].upper() + name[1:]
    else:
        return name[0].upper() + name[1:i] + capitalize(name[i:])

def bondify(name):
    """
    makes a name a lot cooler
    """
    return name[name.find(" ") + 1 : ] + ", " + name

n = "mikhail rudoy"
s = capitalize(n)
print n
print s
print bondify(s)
