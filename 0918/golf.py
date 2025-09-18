'''
Golf scores record the number of strokes used to get the
ball in the hole. The expected number of strokes varies
from hole to hole and is called par
(possible values: 3, 4, or 5).
Each score's name is based on the actual strokes taken
compared to par:

    "Eagle": number of strokes is two less than par
    "Birdie": number of strokes is one less than par
    "Par": number of strokes equals par
    "Bogey": number of strokes is one more than par

Given two integers that represent the number of strokes
used and par, write a program that prints the appropriate
score name. Print "Error" at the end of the output if
par is not 3, 4, or 5, or if the score's name
is not "Eagle", "Birdie", "Par", or "Bogey".
'''

#Special thanks to Garret, Jackson, Elijah, and Jason

# get input
strokes = int(input())
par = int(input())

# store our result for later printing
name = "?"

# make comparisons
if ((par < 2) or (par > 5)):
    name = "Error"
elif (strokes - 1 == par): # this means they got 1 over par
    name = "Bogey"
elif (par == strokes): # the same is par
    name = "Par"
elif (strokes + 1 == par): # 1 less
    name = "Birdie"
elif (strokes + 2 == par): # 2 less
    name = "Eagle"
else:
    name = "Error"

# The output step
print(f"Par {par} in {strokes} strokes is {name}")






  
