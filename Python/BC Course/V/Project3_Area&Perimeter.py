#Project 3 : Area and Perimeter
def function1():
    print ("\nCalculate Perimeter\n1. Circle\n2. Square\n3. Rectangle")
    user = int(input("Choose (1-3): "))

    if user == 1 : 
        r = int(input("Radius: "))
        perimeter = 3.14 * r * 2
        print (perimeter)
    elif user == 2 :
        sides = int(input("Sides: "))
        perimeter = sides*4
        print (perimeter)
    else :
        h = int(input("Height: "))
        w = int(input("Width: "))
        perimeter = 2*(h+w)
        print (perimeter)
        

def function2():
    print ("\nCalculate Area\n1. Circle\n2. Square\n3. Rectangle")
    user = int(input("Choose (1-3): "))

    if user == 1 : 
        r = int(input("Radius: "))
        area = 3.14 * r**2
        print (area)
    elif user == 2 :
        sides = int(input("Sides: "))
        area = sides**2
        print (area) 
    else :
        h = int(input("Height: "))
        w = int(input("Width: "))
        area = h*w
        print (area)
        

def main():
    print ('-'*10, '\nMAIN MENU',)
    print ('-'*10, '\n1. Calculate Perimeter\n2. Calculate Area\n3. Exit')
    user = int(input("Choose (1-3): "))

    if user == 1 :
        function1()
        main()
    elif user == 2 :
        function2()
        main()
    else :
        print ("Thank you!")

main()