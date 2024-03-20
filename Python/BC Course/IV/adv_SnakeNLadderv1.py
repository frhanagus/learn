import random

def roll_die(name, pos) :
    heads = [ 2, 8, 15, 22]
    tails = [12, 5, 24, 11]
    size = len(heads)
    die = random.randint(1,6)
    print (f'{name:10} : {pos} + {die}', end= ' = ')
    pos = pos + die
    for i in range(size) :
        h = heads[i]
        t = tails[i]
        if pos == h:
            print (pos, end=' -> ')
            if h > t :
                print("Hit a snake", end=' -> ')
            else :
                print("Hit ladder", end=' -> ')
            pos = t
            break
        elif pos < h :
            break
    print(pos)
    return pos

# main
n = 5
p1 = 0
name1 = 'Steve'
p2 = 0
name2 = 'Alex'
r = 1
while True :
    print(f'\nRound {r}')
    r += 1
    p1 = roll_die(name1,p1)
    if p1 == n*n :
        print(f'\n{name1} is the winner')
        break
    p2 = roll_die(name2,p2)
    if p2 == n*n :
        print(f'\n{name2} is the winner')
        break        

