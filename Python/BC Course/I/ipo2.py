a, b, c =  input('input a b c: ').split(' ')

#diiketahui a=1 b=5 c=-14

a = float(a)
b = float(b)
c = float(c)

x1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print(x1, x2)