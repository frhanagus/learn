import random

def roll_die(name, pos) :
    heads = [ 2, 8, 15, 22]
    tails = [12, 5, 24, 11]
    size = len(heads)
    die = random.randint(1,6)
    print (f'{name} : {pos} + {die}', end= ' = ')
    pos = pos + die
    for i in range(size) :
        h = heads[i]
        t = tails[i]
        if p1 == h:
            p1 = tails[i]
            print (pos, end=' -> ')
            if h > t :
                print("Hit ladders", end=' ')
            else :
                print("Hit a snake", end=' ')
            pos = t
            print(pos, end=' -> ')
            break
        elif pos < h :
            break
    print(pos)
    return pos

# main
    