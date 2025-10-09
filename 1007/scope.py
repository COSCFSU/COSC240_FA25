'''
    Scope examples
'''
globalx = 10

def doSomeStuff(a, b):
    x = a ** b
    y = "hmm"
    print("x:", x)
    print(globalx)
    for i in range(10):
        print(y)
        z = i

def doOtherStuff(a, b):
    x = "what???"
    print("x:", x)

doSomeStuff(1, 2)
doOtherStuff(1, 2)
