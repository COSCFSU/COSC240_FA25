'''
Loop examples

Authors: SteveK and ...
9/23/2025
'''

#iterators
i = 5
while (i > 0):
    print(i)
    i = i - 1

i = 0
while (i <= 5):
    print(i)
    i = i + 1

i = 2
while (i <= 10):
    print(i, end=" ")
    i = i + 2
print()


#sentinel
keepGoing = False # currently false, to skip it
while (keepGoing):
    word = input(">")
    print(word + "?")
    if (word == "x" or word == "X"):
        keepGoing = False


print("\nSome more examples...")
# ----------------------------------
# Factorial, thanks Tim, Jackson, Jason, Kam, Elijah!
print("Factorial!")

i = 7 # aka 5!
f = 1 # the factorial result
while(i > 0): # some continuation condition?
    f = f * i
    # some operator?
    i -= 1
print(f)

# Thanks Elijah
print("Tree!")
i = 1
shape = "*"
desired_number = 5
while (i <= desired_number):
    print(shape * i)
    i += 1

# ----------------------------
# For loops
# ----------------------------

print("\n--- For loops -------- ")

my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print(num)

for num in my_list:
    print(num + 1)

names = ["Sam", "Frodo", "Gollum", "Saruman"]
for cool_name in names:
    print(cool_name)

for name in names:
    if (name == "Frodo"):
        print("Frodo sucks")
    else:
        print(name)

word = "Lord of the Rings"
my_dict = {
    "main": "Frodo",
    "buddy": "Sam",
    "villain": "Who knows?"
    }

print(word)
for c in word:
    print(c, end=",")
print()

for role in my_dict:
    print(role, ":", my_dict[role])

# range(5) # <- sequence of 0, 1, 2, 3, 4
for i in range(5):
    print(i, end=" ")
print("!")

for i in range(2,10):
    print(i, end=" ")
print("!")

for i in range(0,10, 2):
    print(i, end=" ")
print("!")

for i in range(0,10, 3):
    print(i, end=" ")
print("!")

print("\nExamples with various for loops:")
# Some examples comparing the types of for loops
my_list = ["a", "b", "c", "d", "e"]
for letter in my_list:
    print(letter, end=" ")
print()

print("length:", len(my_list))
for i in range(len(my_list)): #len(my_list) is lengh of list
    print(i, end=":")
    print(my_list[i], end=" ")
print()


print("\nNested Loop")
for i in range(5):
    for j in range(5):
        print(i*j, end=" ")
print()




















