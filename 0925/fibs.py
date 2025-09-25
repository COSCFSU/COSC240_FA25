# Fibonacci numbers
# Authors: SteveK, Jackson, Elijah

'''
    fib[0] = 1
    fib[1] = 1
    fib[n] = fib[n-1] + fib[n-2]
'''

fib = [1, 1] # The fibonacci numbers will go here
# Add a bunch of fib numbers to this list
for i in range(2, 500):
    #fib[i] = fib[i-1] + fib[i-2]
    fib.append(fib[i-1] + fib[i-2])
    
print(fib)
print(f"fib[100] is {fib[100]}!!!")
