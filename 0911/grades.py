# Last example
# Get 3 grades, and give the average grade
mygrades = {
    "name": "Steve's grades",
    "exam1": 0,
    "exam2": 0,
    "exam3": 0
}

# get first grade and put it into mygrades
mygrades["exam1"] = int(input("ex1>"))
mygrades["exam2"] = int(input("ex2>"))
mygrades["exam3"] = int(input("ex3>"))

avg = mygrades["exam1"] + mygrades["exam2"] + mygrades["exam3"]
mygrades["average"] = avg / 3

print(mygrades)

# nice formatted output:
print(f"The average grade for {mygrades['name']} is {mygrades['average']:.2f}") 
