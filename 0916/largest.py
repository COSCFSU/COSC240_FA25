# More branching stuff
# 9/16/25

a = 7
b = 7
c = 7
largest = -1

if ((a > b) and (a > c)):
    largest = a
elif ((b > a) and (b > c)):
    largest = b
elif ((c > a) and (c > b)):
    largest = c
else:
    largest = "none, they are equal"


print(f"The largest number is {largest}")
