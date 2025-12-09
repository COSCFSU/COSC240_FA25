'''
    Algorithm analysis examples.
'''

def linear(n):
    count = 0 # c

    for i in range(n): # n
        # count
        count += 1 # c

    return count # c

def constant(n):
    return 1

# =c + n(n(c)) + c
# =cn^2 + 2c
# =O(n^2)
def quadratic(n):
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count

def cubic(n):
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1

    return count

def logarithmic(n):
    count = 0

    while (n > 0):
        #print(n)
        n = n // 2
        count += 1

    return count
        

n = 20
print(f"n is {n}")
print("Constant count :",constant(n))
print("Linear count :",linear(n))
print("Quadratic count :",quadratic(n))
print("Cubic count :",cubic(n))
print("Logarithmic count :",logarithmic(n))
