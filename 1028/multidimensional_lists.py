'''
Multi-dimensional lists
'''

def runExample():
    onedttt = ['x','x','o','o','o','x','x','o','x']
    print(onedttt)

    twodttt = [
        ['x','x','o'],
        ['o','o','x'],
        ['x','o','x']
        ]
    print(twodttt)

    print2D(twodttt)

def print2D(my2d):
    print("printing...")
    for row in my2d:
        #print(row)
        for c in row:
            print(c, end=" ")
        print()

if __name__ == "__main__":
    runExample()
