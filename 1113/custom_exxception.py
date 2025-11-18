'''
Custom exception
'''
class IDontLikeNegativesError(Exception):
    def __init__(self, value):
        self.value = value


my_num = int(input("Enter number: "))

if my_num < 0:
    raise IDontLikeNegativesError("No way!")
else:
    print(f"num: {my_num}")
