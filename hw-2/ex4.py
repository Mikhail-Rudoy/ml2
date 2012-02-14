def f1(a):
    print "In f1", a
    a = a + 1
    print "In f1", a
    return a

a = 10
print a
a = f1()
print a
