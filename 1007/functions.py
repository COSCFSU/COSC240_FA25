'''
    Functions examples

    COSC 240
    10/7/24

    Authors: SteveK, and friends
'''


# This function will print "word" every time
def sayWord():
    sayThis("word")

# Prints a word provided by caller
#   word - should be a string
def sayThis(word):
    print(word)

# Adds two values and returns the result
#   a - first number
#   b - second number
def add(a,b):
    return a + b

# Conversion function
def convertCtoF(c):
    result = c * 9/5 + 32
    return result

# Prints numbers from 1 to n
def countTo(n):
    for i in range(1, n+1):
        print(i)

def count(n, skip):
    for i in range(1, n+1, skip):
        print(i)

# ----------------------------------------------
# Down here, this code just tests our functions
# ----------------------------------------------
sayWord()
sayThis("Hello")

result = add(1, 1)
print(result)

result = add("1", "1")
print(result)

result = convertCtoF(16)
print(result)

countTo(5)
count(5, 2)
