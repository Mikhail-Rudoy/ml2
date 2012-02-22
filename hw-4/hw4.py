def first_half(str):
    return str[:len(str)/2]

def left2(str):
    return str[2:] + str[:2]

def combo_string(a,b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

def pigWord(word):
    vowels = "aeiou"
    if vowels.find(word[0]) >= 0:
        return word + "yay"
    else:
        return word[1:] + word[0] + "ay"

print "first_half('WooHoo')", first_half("WooHoo")
print "first_half('HelloThere')", first_half("HelloThere")
print "first_half('abcdef')", first_half("abcdef")
print "left2('Hello')", left2("Hello")
print "left2('java')", left2("java")
print "left2('Hi')", left2("Hi")
print "combo_string('Hello', 'hi')", combo_string("Hello", "hi")
print "combo_string('hi', 'Hello')", combo_string("hi", "Hello")
print "combo_string('aaa', 'b')", combo_string("aaa", "b")
print "pigWord('if')", pigWord("if")
print "pigWord('i')", pigWord("i")
print "pigWord('had')", pigWord("had")
print "pigWord('a')", pigWord("a")
print "pigWord('million')", pigWord("million")
print "pigWord('dollars')", pigWord("dollars")
