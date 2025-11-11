'''
    Takes 5 words from the user and stores them in a list, then prints it out.

    This is an example of various things, but specifically exceptions...

    Authors: Steve K & Jackson & Garrett
'''

# function that takes in 5 inputs
def getInputs():
    my_list = []

    for i in range(5):
        user_in = input(f"in{i+1}>")

        try:
            if user_in.isdigit():
                raise TypeError("Woops, we don't like numbers here!")
        except TypeError as e:
            print("No!", e)
            user_in = "ERROR"
        
        my_list.append(user_in)

    return my_list

my_list = getInputs()
print(my_list)
