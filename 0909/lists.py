# Lists
# 9/9/25
# by SteveK and COSC240

# mutable sequence type
# first example of a container type

name = "Jill"
mylist = [1, "hello", 3, 4+1, name, "Jill2"]

print(mylist)
print(mylist[1])

i = 3
print(mylist[i])
i += 1
print(mylist[i])
mylist.append("newstring")
print(mylist)
mylist.pop(2)
print(mylist)
mylist.pop()
print(mylist)
mylist.append("Jill3")
print(mylist)
mylist.remove("Jill")
print(mylist)
print(len(mylist))
mylist2 = [9, 9, 8, 7]
mylist3 = mylist + mylist2
print(mylist3)
print(min(mylist2))
print(mylist2.count(9))
print(mylist2.index(8))


# Average grade
grades = [99, 56, 25, 98, 90, 90]
print("Grades:", grades)
print("Lowest score:", min(grades))
print("Highest score:", max(grades))

# Tuple
# immutable collection
mytuple = (1, 2, 3)
print(mytuple)

# Set
# unordered collection of unique elements
print("Sets!")
set1 = set([1, 2, 3, 4])
set2 = {4, 5, 6}
set3 = {4, "word", 99, 99}
print(set1)
print(set2)
print(set3)

set3.add("newelement")
print(set3)
set3.remove(4)
print(set3)
set3.pop() #remove a RANDOM ELEMENT
print(set3)
set3.update(set1)
print(set3)

# logical behavior or sets
print()
print("set1:", set1)
print("set2:", set2)
print("intersection:", set.intersection(set1, set2))
print("union:", set.union(set1, set2))
print("difference:", set.difference(set1, set2))
