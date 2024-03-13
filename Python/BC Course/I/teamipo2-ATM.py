balance = 500
print('[1. Deposit; 2. Withdraw; 3. Balance; 0. Exit]')
choice = input("What can I help you? ")
choice = int(choice)

if(choice == 1):
    deposit = input('How much? ')
    deposit = int(deposit)
    balance += deposit
    print('Your balance now is',balance)
elif(choice ==2):
    withdraw = input('How Much? ')
    withdraw = int(withdraw)
    balance -= withdraw
    print('Your balance now is',balance)
elif(choice ==3):
    print('Your balance now is',balance)
elif(choice == 0):
    print("Ok then, see you!")
else:
    print("Invalid choice!")