'''
    Street Food program.

    The user will be able to enter the kind of food that they want,
        and we'll give them recommendations.


    Special thanks to Jackson, Theo, Elijah, Jason, et al
    Extra special thanks to Jaala and Dean for deciding to come...
'''

import random

# O read the file
# O load the data
# O load it into some container (dict maybe)
# O put that data somewhere, maybe load it into a list
# O get user input
# O search the records for country name
# O output
#   don't know what it will look like yet



# Read the associated file if it exists, and then
#   return all of that data
def get_data(filename):
    filecontents = open(filename, mode="r", encoding="utf-8")
    the_list = [""] * 4501
    counter = 0

    for line in filecontents:
        row = line.strip().split(',')

        record = {
            "dish": row[0],
            "country": row[1],
            "region": row[2],
            "ingredients": row[3],
            "description": row[4],
            "method": row[5],
            "price": row[6],
            "vegetarian": row[7]
            }
        #print(line)
        #print(record)

        #the_list.append(record) <-- the old way (for comparison)
        the_list[counter] = record
        counter += 1

    return the_list

# This will find out what the user wants to try and give some recommendations
def find_food(food):
    print("Let's find the right food for you!")
    match_list = []


    try:
        # get user input
        user = input("Enter a country:")
        # get all the matches (ignoring case)
        for item in food:
            #   put the food item into a list
            if user == item["country"].lower():
                match_list.append(item)

        #print(match_list)
        print(len(match_list), "matches found!")

        # get a random food record
        r = random.randint(0, len(match_list)-1)
        
        # print
        #print(match_list[r])
        print(f'What about: {match_list[r]["dish"]} from {match_list[r]["region"]}?')
    except(ValueError):
        print("Sorry, we don't have data for there...")


















if __name__ == "__main__":
    food = get_data("global_street_food.csv")
    #print(food[10])
    find_food(food)
    
