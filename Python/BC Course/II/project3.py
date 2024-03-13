#Project 3 : Movie Ticket Calculator

print("Welcome to Movie Ticket Calculator!")
print("Please enter your age and select the movie time to calculate the cost of the movie ticket.")
age = int(input("Enter your age: "))
if age < 13:
    origin_price = 5
    movie_price = 5
    condition = "Child"
elif age >= 13 and age < 65:
    origin_price = 10
    movie_price = 10
    condition = "Adult"
else:
    movie_price = 7
    origin_price = 7
    condition = "Senior"
print("\nMovie Time Options: \n1. Morning (9:00 AM - 12:00 PM)\n2. Afternoon (12:00 PM - 6:00 PM)\n3. Evening (6:00 PM - 10:00 PM)\n4. Night (10:00 PM - 12:00 AM)")
movie_time = int(input("Select the movie time (1-4): "))
if movie_time == 1:
    movie_price = movie_price * 90 / 100
elif movie_time == 3:
    movie_price = movie_price + (movie_price * 20 / 100)
elif movie_time == 4:
    movie_price = movie_price + (movie_price * 50 / 100)
else:
    movie_price = movie_price
print(f'You are {condition}. The base cost of your movie is ${origin_price}. \nYour total ticket cost is: ${movie_price}, Enjoy the movie!')