'''
    This is our example code that we can then use to figure
        out how it works in our project.

    authors: SteveK and COSC240
    10/23/2025
'''

# this will read a file and return its contents
def getFile(filename):

    cartoons = open(filename, mode='r', encoding="utf-8")
    contents = cartoons.readlines()
    cartoons.close()

    return contents

# main function
def main():
    cartoons = getFile("Cartoons.csv")

    #print(cartoons)
    print(cartoons[0])
    print(cartoons[1])

# run the program
main()
