
# --------------
word = "hello"
length = len(word)
i = 0
while (i < length):
    print(word[i])
    i += 1

i = len(word)-1 # start at end
while(i >= 0):
    print(word[i], end=" ")
    i = i - 1
print()
