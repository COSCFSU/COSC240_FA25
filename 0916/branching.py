# Python branching logic examples
# SteveK & COSC240 class
# 9/16/25
#
#   Show examples of how to use if and Boolean expressions

# This program will check your grade and tell you
#   the letter grade.

# get input, thanks Jack, Jason, and Theo
grade = input("What is your grade? >") # string
grade = float(grade) # float
letter = "?" # thanks, Elijah

# determine letter, thanks Cam, Jason, Tim, Elijah, Garett, Riley
if (grade < 60.0):
    letter = "F"
elif (grade < 70.0):
    letter = "D"
elif (grade < 80.0):
    letter = "C"
elif (grade < 90.0):
    letter = "B"
else:
    letter = "A" 

# print result
print(f'Your grade of {grade} is {letter}')
