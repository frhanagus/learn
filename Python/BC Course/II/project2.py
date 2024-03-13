#Project 2 : Simple Calculator

print("WELCOME TO SIMPLE CALCULATOR")
print(f'1.Addition')
print(f'2.Subtraction')
print(f'3.Multiplication')
print(f'4.Division')

choice = int(input("input your choice (1-4)"))
n1 = int(input("first number ="))
n2 = int(input("second number ="))


if(choice ==  1 ):
  result = n1+n2
  print(f'{n1} + {n2} is {result}')

elif(choice ==  2 ):
  result = n1-n2
  print(f'{n1} - {n2} is {result}')

elif(choice ==  3 ):
  result = n1*n2
  print(f'{n1} * {n2} is {result}')

elif(choice ==  4 ):
  result = n1/n2
  print(f'{n1} / {n2} is {result}')