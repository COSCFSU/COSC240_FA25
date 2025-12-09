'''
    Write a program that takes an integer list as input and sorts the list into descending order using selection sort. The program should use nested loops and output the list after each iteration of the outer loop, thus outputting the list N-1 times (where N is the size of the list).

    Ex: If the input is:

    20 10 30 40

    the output is:

    [40, 10, 30, 20]
    [40, 30, 10, 20]
    [40, 30, 20, 10]

    Ex: If the input is:

    7 8 3

    the output is:

    [8, 7, 3]
    [8, 7, 3]

    Note: Use print(numbers) to output the list numbers and achieve the format shown in the example.
'''


'''
# First book version
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
    
        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
'''
def selection_sort(numbers):
    print("sort!")
    for i in range(len(numbers) - 1):
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j

        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp
        print(numbers)


my_list = [20, 10, 30, 40]
selection_sort(my_list)
























