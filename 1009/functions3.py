'''
    functions even more
'''

# generic function for example
def doExampleAgain(name, number, word):
    print(name, number, word)

# default parameter
def doOtherExample(name, number, word="What!?"):
    print(name, number, word)

# this one uses arbitrary args
def doEx3(word="what?", *args):
    print(word, args)
    if (len(args) > 0):
        print("yay!->", args[0])

# multiple returns
def doEx4():
    return 1, 2, 3

# normal function call
doExampleAgain("Bob", 999, "Hello")
# function call using keyword arguments
doExampleAgain(name="Bob", word="Hello", number=999)

print("second example:")
doOtherExample("Bob", 999, "Hello")
doOtherExample("Bob", 999)

print("third example, on arbitrary arguments")
doEx3("hello", "omg", "wtf", "lol")
doEx3()

print("ex4 is about multiple returns:")
print(doEx4())
a,b,c = doEx4()
print(a, b, c, "!")
