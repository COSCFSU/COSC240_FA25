'''


Write a program that takes in a positive integer as input,
and outputs a string of 1's and 0's representing the
integer in binary. For an integer x, the algorithm is:

As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2

Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function to reverse the string.

Ex: If the input is:

6

the output is:

110

The program must define and call the following two functions. Define a function named int_to_reverse_binary() that takes an integer as a parameter and returns a string of 1's and 0's representing the integer in binary (in reverse). Define a function named string_reverse() that takes an input string as a parameter and returns a string representing the input string in reverse.
def int_to_reverse_binary(integer_value)
def string_reverse(input_string)

Authors: SteveK and COSC240 class
'''

# takes an int and returns a string of 1's and 0's
def int_to_reverse_binary(x):
    '''
        As long as x is greater than 0
           Output x % 2 (remainder is either 0 or 1)
           x = x // 2
    '''
    binary_string = "" # an empty string
    while(x > 0):
        #print(x%2)
        # add the bit to the string
        binary_string = binary_string + str(x%2)
        x = x // 2
    #print("->", binary_string) # test output... TODO: erase this
    return binary_string

# takes an input string, and returns it in reverse
def string_reverse(s):    
    temp_string = ""
    for ch in s:
        #print(ch, "?")
        temp_string = ch + temp_string
    return temp_string

n = 127
the_binary = int_to_reverse_binary(n)
the_binary = string_reverse(the_binary)

print("is it right? ->", n, "->", the_binary)





















