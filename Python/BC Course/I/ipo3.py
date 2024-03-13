import math as m


n, r = input('input n and r: ').split(' ')
a = int(n)
b = int(r)

P = (m.factorial(a))/(m.factorial(a-b))

C = (m.factorial(a))/((m.factorial(b))*((m.factorial(a-b))))


print(n, "P", r, '=', P )

print(n, "C", r, '=', C )


