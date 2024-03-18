# functions
'''
def f(x) :
    y = 3 * x
    return y

# main
x = 2
result = f(x)
print(result)
'''
#1
def f1(x) :
    y = x**3
    return y

def f2(x, y) :
    z = x**y
    return z

def f3(x, y) :
    z = 5 * x + 2 * y
    return z

def f4(x) :
    y = x**2 + 4*x - 3
    return y

def f5(a, b) :
    c = (a**2 + b**2)**0.5
    return c

x = 3
y = 4
a = x
b = y
result1 = f1(x)
result2 = f2(x, y)
result3 = f3(x, y)
result4 = f4(x)
result5 = f5(a, b)
print(f'1. y = x^3 : ', result1)
print(f'2. z = x^y : ', result2)
print(f'3. z = 5x + 2y : ', result3)
print(f'4. y = x^2 + 4x -3 : ', result4)
print(f'5. c = sqrt(a^2 + b^2) : ', result5)