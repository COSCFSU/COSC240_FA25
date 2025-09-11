# Dict example 2

bulbasaur = {
    "name": "Bulbasaur",
    "dexno": 1,
    "str": 10,
    "max_hp": 100
}

naruto = {
    "name": "Naruto Uzumaki",
    "str": 100,
    "max_hp": 100
}

print(naruto)

bulbasaur["int"] = 1
naruto["int"] = 10

coolcharacters = [naruto, bulbasaur]

print(naruto)
del naruto["str"]
print(naruto)
