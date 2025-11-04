'''
Write a function driving_cost() with parameters miles_per_gallon,
dollars_per_gallon, and miles_driven, that returns the dollar cost to
drive those miles. All items are of type float. The function called with
arguments (20.0, 3.1599, 50.0) returns 7.89975.

The main program's inputs are the car's miles per gallon and the price of gas
in dollars per gallon (both float). Output the gas cost for 10 miles, 50 miles,
and 400 miles, by calling your driving_cost() function three times.

Output each floating-point value with two digits after the decimal point,
which can be achieved as follows:
print(f"{your_value:.2f}")

Ex: If the input is:

20.0
3.1599

the output is:

1.58
7.90
63.20

Your program must define and call a function:
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)

'''

#  calculates cost of driving your car based on gas
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    dollar_cost = miles_driven / miles_per_gallon * dollars_per_gallon
     
    return dollar_cost

'''


Define a function named swap_values that takes four integers as parameters and swaps
the first with the second, and the third with the fourth values. Then write a main
program that reads four integers from input, calls function swap_values() to swap
the values, and prints the swapped values on a single line separated with spaces.

Ex: If the input is:

3
8
2
4

function swap_values() returns and the main program outputs:

8 3 4 2

The program must define and call the following function.
def swap_values(user_val1, user_val2, user_val3, user_val4)

'''

def swap_values(user_val1, user_val2, user_val3, user_val4):
    a_blank_list = [user_val2, user_val1, user_val4, user_val3]

    for val in a_blank_list:
        print(val, end=' ')

# First Example
#result = driving_cost(20.0, 3.1599, 50.0)
#print(f"{result:.2f}")

# Second Example
#swap_values(3, 8, 2, 4)

# Third Example - Bubble Sort
def bubblesort(my_list):
    # compare 2 numbers, moving the lower one to the left...
    #   then repeat that n or so times

    n = len(my_list)
    for i in range(n):
        # print(i, '->')
        for j in range(n - 1):
            # print(' ', j)
            if (my_list[j] > my_list[j+1]):
                # print('swap')
                swap(my_list, j, j+1)

# Fourth Example - Selection Sort
# we have two parts of the list, sorted and unsorted
#   One by one, put the [largest] element at the back of the unsorted part of the list,
#       and then moves the marker up
def selectionsort(my_list):

    n = len(my_list)
    for i in range(n): # every element gets compared
        #print(' ', i, ':', end=' ')
        largest = 0 # so far, this is the position of the largest
        # Find the largest element
        for j in range(n - i): 
            #print(j)
            if (my_list[largest] < my_list[j]):
                largest = j
        # largest now points to the largest element, so swap
        #print("Largest:", my_list[largest], end='-')
        swap(my_list, n - i - 1, largest)
        #print(f"{my_list}, <- Largest:{largest}, Mark:{n - i - 1}")

# a swap function, so we can swap stuff
def swap(a_list, a, b):
    tmp = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = tmp

another_list = [5, 4, 3, 2, 1]
print(another_list, "<- BUBBLE SORT!")
bubblesort(another_list)
print(another_list)

#another_list = [9, 8, 1, 2, 99, 88, 11, 22, 5, 77]
another_list = [7, 1, 5, 2, 4, 3]
print(another_list, "<- SELECTION SORT!")
selectionsort(another_list)
print(another_list)






































