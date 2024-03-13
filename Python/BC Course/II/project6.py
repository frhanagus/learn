#Project 6 : Shipping Cost Calculator
br_std = 5.00
br_exp = 15.00
rpp = 2.00
rpm = 0.50

print ("Welcome to the Shipping Cost Calculator!\nPlease enter the weight of your package and the distance to be shipped.")
w = float(input("Enter the weight of the package (in pounds): "))
d = float(input("Enter the shipping distance (in miles): "))
wprice = (rpp*w)
dprice = (rpm*d)

print ("\nSelect Shipping Method:\n1. Standard Shipping\n2. Express Shipping")
choice = input("Enter your choice (1 or 2): ").lower()

if w >= 10 :
    wfinal_price = (90/100) * wprice
else : wfinal_price = wprice

if d >= 500 :
    dfinal_price = (80/100) * dprice
else : dfinal_price = dprice

if choice == "1":
    price = br_std + wfinal_price + dfinal_price
elif choice == "2":
    price = br_exp + wfinal_price + dfinal_price
else : 
    print("Sorry, that option is unavailable")
    quit()

if dfinal_price == (80/100) * dprice :
    print ("You received a 20% discount for a package over 500 miles.")
if wfinal_price == (90/100) * wprice :
    print ("You received a 10% discount for a package over 10 pounds.")

print (f'\nThe shipping cost for your package is: $',price)