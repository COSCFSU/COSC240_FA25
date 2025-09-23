# Algorithms!
#
# Authors: SteveK, Jackson, Theo, Elijah, Tim
# 9/23

print("-- SEQUENTIAL SEARCH (aka linear search) --")

my_list = [5, 2, 7, 19, 1, 55, 100]
t = 19
for num in my_list:
    print(num, end=" ")
    if (num == t):
        print("found it!")
        break
print("---")


print("-- BUBBLE SORT --")
my_list = [5, 4, 3, 2, 1]
my_list2 = [1, 100, 2, 55, 35, 77, 21, 99]

my_list = my_list2
# bubble action
for j in range(len(my_list)-1):
    for i in range(len(my_list)-1):
        #print(i) # show index
        #print(f"{my_list[i]}, {my_list[i+1]}")
        if(my_list[i] > my_list[i+1]):#?
            # when the first one is larger, we swap the values
            temp = my_list[i+1]
            my_list[i+1] = my_list[i]
            my_list[i] = temp
    print(my_list)
print(my_list)
