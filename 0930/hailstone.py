# Hailstone sequence

'''
Given a positive integer n, the following rules will always create a sequence that ends with 1, called the hailstone sequence:

    If n is even, divide it by 2
    If n is odd, multiply it by 3 and add 1 (i.e. 3n +1)
    Continue until n is 1

Write a program that reads an integer as input and prints the hailstone sequence starting with the integer entered. Format the output so that five integers, each separated by a tab character (\t), are printed per line. End the output with a tab character.

The output format can be achieved as follows:
print(n, end='\t')
'''

n = 25
count = 0
print(n, end="\t")
while (n > 1):
    if (n % 2 == 0): # aka even
        n = n // 2
    else: # aka odd
        n = (3*n)+1
    count += 1
    if (count == 5): # on the 5th num, make a new line
        print() # new line
        count = 0
    print(n, end="\t")


