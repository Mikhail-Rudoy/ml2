def pigWord(word):
    shouldCAP = (word[:1] == word[:1].upper())
    word = word.lower()
    
    letters = "qwertyuiopasdfghjklzxcvbnm"
    i = len(word) - 1
    while i >= 0 and letters.find(word[i]) == -1:
        i = i - 1
    if i == -1:
        return word
    punctuation = word[i+1:]
    word = word[:i+1]
    
    vowels = "aeiou"
    if vowels.find(word[0]) >= 0:
        word = word + "yay" + punctuation
    else:
        word = word[1:] + word[0] + "ay" + punctuation
    
    if shouldCAP:
        return word[:1].upper() + word[1:]
    else:
        return word

def pigLatin(sentence):
    l = sentence.split(" ")
    for i in range(len(l)):
        l[i] = pigWord(l[i])
    return " ".join(l)

print "pigWord('If') =", pigWord("If")
print "pigWord('I') =", pigWord("I")
print "pigWord('had') =", pigWord("had")
print "pigWord('a') =", pigWord("a")
print "pigWord('million') =", pigWord("million")
print "pigWord('Dollars!') =", pigWord("Dollars!")
print "pigLatin('If I had a million dollars ($), I would be rich!!') =", pigLatin('If I had a million dollars ($), I would be rich!!')
