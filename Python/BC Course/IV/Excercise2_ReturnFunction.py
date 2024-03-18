# rumus abc
import math

# input function
def getInput(text) :
    while True :
        num = float(input("\nInput " + text + ": "))
        if (text == "a" and num == 0) :
            print('a cannot be 01')
        else :
            return num

# process function
def getDiscriminant() :
    while True :
        a = getInput("a")
        b = getInput("b")
        c = getInput("c")
        d = b**2 - 4*a*c
        if d < 0 :
            print('\nD =', d)
            print('Invalid discriminant')
        else :
            return a,b,c,d

#process function
def getX1X2(a,b,d) :
    p = math.sqrt(d)
    x1 = (-b + p) / (2 * a)
    x2 = (-b - p) / (2 * a)
    return x1, x2

# output function
def printResult(a,b,c,x1,x2) :
    a = int(a)
    b = int(b)
    c = int(c)
    print(f'\n{a}x^2 + {b}x + {c} = 0')
    print(f'x1 = {x1}, x2 = {x2}')

a,b,c,d = getDiscriminant()
x1, x2 = getX1X2(a,b,d)
printResult(a,b,c,x1,x2)