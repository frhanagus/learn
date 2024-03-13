import random

me = int(input("Choose 1)Rock, 2)Paper, or 3)Scissors: ").lower())
comp = int(random.randint(1,3))

if me == int("1"):
    print("You chose Rock")
elif me == int("2"):
    print("You chose Paper")
else : print("You chose Scissors")

if comp == int("1"):
    print("Computer chose Rock")
elif comp == int("2"):
    print("Computer chose Paper")
else : print("Computer chose Scissors")

if me == comp:
    print("It's a tie!")
elif (me == int("1") and comp == int("3")) or \
   (me == int("2") and comp == int("1")) or \
   (me == int("3") and comp == int("2")):
    print("You win!")
else:
    print("You lose!")
