# calculate factorial
# e.g. 5!
#   5! = 5 * 4! = 5 * 4 * 3 * 2 * 1

i = 5
factorial = 1
while(i > 0):
    print(i)
    factorial = factorial * i
    i -= 1

print(f"5! = {factorial}")


'''
# ------------------------------------------------
# longer than
# ------------------------------------------------
a = input("1>") # in zybooks, remove prompt
b = input("2>")

alength = len(a)
blength = len(b)

if(alength > blength):
    print(f"{a} is longer than {b}")
elif(blength > alength):
    print(f"{b} is longer than {a}")
else:
    print(f"{a} {b} are the same length")
'''

# ------------------------------------------------
# four numbers, count odds
# ------------------------------------------------

nums = []

# get 4 inputs
nums.append(int(input(">")))
nums.append(int(input(">")))
nums.append(int(input(">")))
nums.append(int(input(">")))
print(nums)

counter = 0
# look at every number
for n in nums:
    # check if it is odd
    if (n % 2 == 1):
        counter += 1
# if it is odd, increment a counter
print(counter)








