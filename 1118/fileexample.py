'''
Files
'''

def readFile(filename):
    file = open(filename, mode="r", encoding="utf-8")
    #contents = file.read()

    #for line in file:
    #    print(line)

    #print("?")
    return file

def getDictionary(file):
    the_dictionary = {}
    # get every line, storing words in the dictionary
    for line in file:
        #print(line.strip().split(','))
        translation = line.strip().split(',')
        #print(translation)
        the_dictionary[translation[0]] = translation[1]
    
    return the_dictionary

def runTranslationProgram(my_dictionary):
    print("Welcome to my translation program!")
    eng = input("Please enter a word in English>")

    try:
        print("That is:", my_dictionary[eng])
    except(KeyError):
        print("We dont' have that word in the dictionary.")

#file = readFile("eng_fre.csv")
file = readFile("eng_jap.csv")
my_dictionary = getDictionary(file)
#print(contents)
#print(my_dictionary)
#print(my_dictionary["Hi."])
runTranslationProgram(my_dictionary)
