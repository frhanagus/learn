import random

me = input("Choose 1)Rock, 2)Paper, or 3)Scissors: ").lower()
comp = random.randint(1,3)

if me == "1":
    print("You chose Rock")
elif me == "2":
    print("You chose Paper")
else : print("You chose Scissors")

if comp == "1":
    print("Computer chose Rock")
elif comp == "2":
    print("Computer chose Paper")
else : print("Computer chose Scissors")

if me == comp:
    print("It's a tie!")
elif (me == "1" and comp == "3") or \
   (me == "2" and comp == "1") or \
   (me == "3" and comp == "2"):
    print("You win!")
else:
    print("You lose!")
