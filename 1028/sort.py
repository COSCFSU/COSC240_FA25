'''
    Insertion sort.

    Practicing list use with a new sorting algorithm.

    Authors: Steve K and COSC 240 2025 class
'''

# This will sort the list provided, using the insertion sort algorithm
def insertionSort(my_list):
    # start with the index 1, look at each number going left
    # compare numbers (two at a time), switching if the left is larger
    #   stopping, if the left is less (aka it is in the right spot)
    # note: we'll need 2 loops, one for looking to the left, one for going right

    n = len(my_list)
    for i in range(1,n): # go right (we need a variable that stores our starting values
        #print(i)
        current = my_list[i]
        for j in range(i-1, -1, -1): # go left
            #print(j)
            left = my_list[j]
            if left > current:
                #swap!
                temp = my_list[j]
                my_list[j] = current
                my_list[j+1] = temp # temp, not left, because left was already changed

# Returns True if list is sorted, False otherwise
def isSorted(my_list):
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i-1]:
            return False
    return True

# Start the program.  This syntax means,
#   it will only run directly (i.e. not when loaded as a module)
if __name__ == "__main__":
    # some lists for testing
    a = [5, 1, 9, 2, 4]
    a2 = [89, 87, 32, 11, 44, 23, 99, 21]
    a3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    a = a3 # pick list to test
    
    print("Before sort: ", a)
    print(isSorted(a))

    insertionSort(a)
    
    print("After sort:  ", a)
    print(isSorted(a))
