# Letter L
for row in range(5):
    for col in range(5):
        if (row==4 or col==0):
            print(end="#")
        else:
            print(end=" ")
    print ()
print ()
# Letter F
for row in range(5):
    for col in range(5):
        if (col==0 or row==0 or row== 2):
            print(end="#")
        else:
            print(end=" ")
    print ()
print ()
# Letter A
for row in range(5):
    for col in range(5):
        if ((col==2 and row==0) or (col==1 and row==1) or (col==3 and row==1) or (col==0 and row==2) or (col==4 and row==2)):
            print(end="#")
        else:
            print(end=" ")
    print ()
print ()