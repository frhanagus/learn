#Project 5 : Snake and Ladder

import random 
import time
turn = 0
pos = 0 
win = 0
pName = 'Wening'

while win == 0:
    time.sleep(1)
    dice = random.randint(1,6)
    print(f'{pName:10}:{pos} + {dice}')
    pos = pos + dice
    if pos == 5:
        pos = 15
    elif pos == 10:
        pos = 3
    elif pos == 12:
        pos = 21
    elif pos == 24:
        pos = 13
    elif pos == 25:
        win = 1
    elif pos > 25:
        pos = 25 - (pos -25)
    print("New position:", pos)
    turn = turn + 1

print(f'Yeay, you win. \nYou finished in {turn} turn')