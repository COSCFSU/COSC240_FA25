'''
    Exceptions and Defensive Programming------------

    author: Steve K & COSC 240
'''

def run_example():
    print("Exception first example vvv")

    '''
        print("try block\n")
        userin = input("Enter a number>")
        num = float(userin)
        print("The num was", num)
        print(num - "hello")
    '''
    try:
        print("try block\n")
        userin = input("Enter a number>")
        num = float(userin)
        print("The num was", num)
        print(num - "hello")
    except ValueError as e:
        print("There was a value error... :(")
        print("error:", e)
    except TypeError:
        print("Woops!  Type error, it shouldn't be a number afterall...")
    except:
        print("except block\n")
    finally:
        print("\nfinally block\n")
        
    print("hello")

def a():
    print("a")
    try:
        b()
    except TypeError as e:
        print("C didn't work because of", e)

def b():
    print("b")
    c()

def c():
    print("c")
    raise TypeError("IDK, some error")

#run_example()
a()














