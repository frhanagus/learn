import random

print ("Rock, Paper, Scissors\n")
turn = int(input("How many times you wanna play ?( 2-10 ): "))
ronde = 1
Human_Score = 0
Bot_Score = 0

for turn in range (0,turn) :
    print()
    print (f'Round #', ronde)
    me = int(input("Input 1-Rock, 2-Paper, 3-Scissors: "))
    comp = int(random.randint(1,3))
    ronde += 1
    
    if me == int("1"):
        print("Human = Rock")
    elif me == int("2"):
        print("Human = Paper")
    else : print("Human = Scissors")

    if comp == int("1"):
        print("Bot = Rock")
    elif comp == int("2"):
        print("Bot = Paper")
    else : print("Bot = Scissors")

    if me == comp:
        print("It's a tie!")
    elif (me == int("1") and comp == int("3")) or \
    (me == int("2") and comp == int("1")) or \
    (me == int("3") and comp == int("2")):
        print("You won this round")
        Human_Score += 1
    else:
        print("You lost this round")
        Bot_Score += 1

print ()
print ('Final Result\n')
print ('-'*10)
print (f'Human =',Human_Score)
print (f'Bot =',Bot_Score)
print ('-'*10)

if Human_Score > Bot_Score :
    print ("You are the winner!")
elif Human_Score < Bot_Score: 
    print ("Bot wins!")
else :
    print ("It's a tie!")
