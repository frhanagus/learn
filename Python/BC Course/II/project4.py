#Project 4 : Ticket Vending Machine

print("Welcome to Lee's Ticket Vending Machine")
ticketPrice = float(input("How much is the ticket price? "))
payment = float(input("Pay how much? "))

change = payment - ticketPrice
print(f"Change = {change}")

cents = int(change * 100)
if(cents >= 100):
    if(cents >= 1000):
        tenBill = cents // 1000
        cents -= tenBill * 1000
        print(f"{tenBill} bill(s) of $10")
        
    if(cents >= 500):
        fiveBill = cents // 500
        cents -= fiveBill * 500
        print(f"{fiveBill} bills(s) of $5")
        
    if(cents >= 200):
        twoBill = cents // 200
        cents -= twoBill * 200
        print(f"{twoBill} bills(s) of $2")
        
    if(cents >= 100):
        oneCoin = cents // 100
        cents -= oneCoin * 100
        print(f"{oneCoin} coin(s) of $1")
        
    if(cents >= 50):
        fiftyCent = cents // 50
        cents -= fiftyCent * 50
        print(f"{fiftyCent} coin(s) of 50c")
        
    if(cents >= 20):
        twentyCent = cents // 20
        cents -= twentyCent * 20
        print(f"{twentyCent} coin(s) of 20c")
        
    if(cents >= 10):
        tenCent = cents // 10
        cents -= tenCent * 10
        print(f"{tenCent} coin(s) of 10c")
        
    if(cents >= 5):
        fiveCent = cents // 5
        cents -= fiveCent * 5
        print(f"{fiveCent} coin(s) of 5c")
        
    if(cents >= 1):
        oneCent = cents // 1
        cents -= oneCent * 1
        print(f"{oneCent} coin(s) of 1c")