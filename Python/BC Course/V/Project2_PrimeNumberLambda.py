# Prime number detecter with lambda
def detect() :
    numbers = [1,2,3,4,5,6,7,8,9]
    p = input('Enter a number (or type "exit" to quit): ').lower()
    num = int(p)
    is_prime = lambda n: all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    def is_prime() :

    while True :
        if p == "exit" :
            print (f'Exiting program.')
            break
        elif 
        is_prime(num):
            print (f'{p} is a prime number')
            detect()
        else :
            print (f'Invalid input. Please enter a valid number or type "exit" to quit.')
            detect()
detect()

#kavya
num = None
def get_input():   
        user_input = input('Enter a number (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            return None
        else:
            return int(user_input)

check_prime = lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

while True:
    num = get_input()
    if num == None:
        break
    if check_prime(num) == True:
        print(f'{num} is prime')
        break
    else:
        print(f'{num} is not prime')