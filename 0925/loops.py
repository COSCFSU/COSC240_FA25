# Loops continued
# Authors: SteveK, Kam, Theo, Dean, Jackson

# -------------------
# Counting numbers
for i in range(1,6):
    print(i, end=" ")
print()

for i in range(1,6,2):
    print(i, end=" ")
print()

# the same as while loops
x = 0
while(x < 5):
    x = x + 1
    print(x, end=" ")
print()

x = 1
while(x <= 5):
    print(x, end=" ")
    x = x + 2
print()

# ------------------------
# Nested Loops
for i in range(100):
    print(i, end=" ")
print()

for i in range(10):
    for j in range(10):
        print(10*i + j, end=" ")
print()

for i in range(10):
    for j in range(10):
        x = 10*i + j
        print(f'{x:2d}', end=" ")
    print()
print()

# Multiplication table
for i in range(1,13):
    for j in range(1,13):
        x = i*j
        print(f'{x:3d}', end=" ")
    print()
print()























