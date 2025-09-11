# Strings and things
# sequence types, thanks Jackson

word = "Hello" # <-- literal

print(word)
print("whatever")

verb = "sniff"
noun = "boat"
name = "Bob"
place = "France"

madlib = f"{name} {verb}ed the {noun} in {place}"
print(madlib)

string_with_spaces = "hello          "

print("length of name:", name, len(name))
print("length of other string:", string_with_spaces, len(string_with_spaces))

#indexing
print(place[0])
print(place[3])
print(place[-1])
print(place[-2])

#concatenation, thanks Braylin and Tim
concat_word = noun + name
print(concat_word)

mynum = 5
print(verb + str(mynum))

# Formatting string
# f-strings
madlib = f"{name} {verb}ed the {noun} in {place}" #replacement fields
print(madlib)

print(f"{2**2=}") # usually we only do this when debugging
print(f"{2**2}")
print(f"{{place}}")

name = "Joe"
num = 7111000
print(f"{name:s}") # s means string presentation
print(f"{num:,d}") # d means decimal presentation, comma puts commas
print(f"{num:020d}") # fill in with 0's
print(f"{num:b}") # b means binary presentation
print(f"{num:x}") # x or X means hexadecimal
print(f"{num:e}") # scientific notation
print(f"{num:f}") # floating point to 6 digits
print(f"{num:.2f}") # 2 digits floating point
print(f"{num:,.2f}") # same ^ but with comma decorators
