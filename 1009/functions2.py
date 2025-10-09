'''
    More function stuff
'''

# pass-by-assignment
def doExample(a, b, c):
    a = "?"
    b = "!"
    c = "!?"
    print(a,b,c)

outsideA = 1
outsideB = 2
outsideC = 3
#doExample(outsideA, outsideB, outsideC)
#print(outsideA, outsideB, outsideC)

# pass-by-assignment pt 2
def doExample(a):
    a[0] = "?"
    a[1] = "!"
    a[2] = "?!"
    print(a)

outsideA = [1, 2, 3]
print("before:", outsideA)
doExample(outsideA)
print("after:", outsideA)

