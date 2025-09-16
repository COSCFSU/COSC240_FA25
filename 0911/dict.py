# Dictionary example
# 9/11

# Dictionary is a container that associates keys to values

somelist = [1, 21, 31]

# key: value pairs, kv pair
thisclass = {
    "Theo": 1,
    "Kevin": 21,
    "Sean": 31
}

print(somelist)
print(thisclass)

candy = {
    "Mr. Goodbar": 1.0,
    "Swedish Fish": .5,
    "Skittles": 1.5,
    "Snickers": 2.0
}

genericdict = {
    5: 5,
    6: 6,
    7: 7
}
print(candy)
print(genericdict)

print(candy["Swedish Fish"])
# print(candy[1.0]) <-- doesn't work, can't go value to key


# Dicts are mutable, some examples:
candy["Swedish Fish"] = .1
print(candy["Swedish Fish"])
candy["Starburst"] = 1.55
print(candy)

del candy["Skittles"]
print(candy)

# Lots of different types that we know:

# numbers
i = 9 # int
f = 9.9 # floating point number

# sequence types
st = "this is a string"
ls = [1,2,3] # list
tu = (1,2,3) # tuple
st = {1,2,3} # set

# mapping type
di = {1:1,2:2,:3} # dict





























