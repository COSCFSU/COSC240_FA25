'''
    Some more list things

    Author: SteveK + others
'''

def runExample(my_list):
    # Standard way to add 1 to every element
    print("Before:", my_list)

    for i in range(len(my_list)):
        my_list[i] = my_list[i] + 1

    print("After:", my_list)

    # Weird Python way of doing this
    print("List Comprehension")
    my_list2 = [(i+1) for i in my_list]
    print("my_list1:", my_list)
    print("my_list2", my_list2)


# Run a binary search, returning the index of target
def binarySearch(my_list, target):
    beg = 0
    end = len(my_list) - 1

    #print("Before search")
    #print(f"beg:{beg}, end:{end}")

    # get the middle value
    # compare middle
    #   if tar > mid
    #       make new list of right
    #   else if tar < mid
    #       make new list of left
    #   else if mid == tar
    #       found
    while beg <= end:

        mid = (beg + end) // 2

        if (target > my_list[mid]):
            beg = mid + 1

        elif (target < my_list[mid]):
            end = mid - 1

        elif (target == my_list[mid]):
            print("Found it!")
            return mid


    #print("After search")
    #print(f"beg:{beg}, end:{end}")

    #   else not found
    print("Not found... :(")
    return -1

def goInCircles(my_list):
    print("This list: ->", my_list)
    count = 0

    while count < len(my_list):
        print(my_list)
        # inner loop moves first element to the end
        for i in range(len(my_list)-1): # dunno yet <-- need to change 4
            t = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = t

            '''

            This is the code that the loop needs to be able to do
            
            t = my_list[1]
            my_list[1] = my_list[2]
            m_list[2] = t

            t = my_list[2]
            my_list[2] = my_list[3]
            my_list[3] = t

            t = my_list[3]
            my_list[3] = my_list[4]
            my_list[4] = t

            t = my_list[4]
            my_list[4] = my_list[5]
            my_list[5] = t
            '''            
            
        #print(my_list[0], end=" ")

        count += 1
    print()
    

if __name__ == "__main__":
    #my_list = [1, 2, 3, 4, 5, 6, 7]
    my_list = [1,2,3,4,5]
    # Example 1
    #runExample(my_list)

    # Example 2
    #tar = 3
    #idx = binarySearch(my_list, tar)
    #print(f"Binary Search: Found {tar} at {idx} in {my_list}!")

    # Example 3
    goInCircles(my_list)
    
