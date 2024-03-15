#6 10 14 18
n = 6
while n < 18:
    print(f'{n} ', end='')
    n += 4
print(f'{n}')

#1 4 256 3125, clue: n^n
n = 1
while n < 6:
    if n != 3:
        print (f'{n**n} ', end='')
    n += 1

