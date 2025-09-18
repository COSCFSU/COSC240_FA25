# More conditional examples
import math

x = 111
y = 111.0


#uservalue = input("value>")

if (x == y):
    print("equal")
else:
    print("not")

#if (x == uservalue):
#    print("equal")
#else:
#    print("not")

fruits = ["apple", "date", "starfruit"]

if ("apple" in fruits):
    print("yes, we have that")
else:
    print("nope")

word = "This has some words in it: frog, bus, camera"

if ("frog" in word):
    print("yes, that is in the string")
else:
    print("nope")



# relational operators have lower precedence than arithmetic
a = 1
b = 1
c = 1

if (a + b == b + c == 2):
    print("yes")
    print("this is a statement")
    print("This is another statement")
else:
    print("Hmm... where is this?")

sentence = ("dflksjflskdjflsdkfjsldkfjsldfkjsdlfksjdfldkjf"
            "xxxxxxksjdlfksjdflskjdflskdfj"
            "sldkfjsldkfjsldfkjsldfkjdlksjdf")
print("what about this?")
print(sentence)

x = math.pow(5,
             2)
print(x)

x = 1
y = '?'
y = 5 if (x == 2) else 1
print(y)


















