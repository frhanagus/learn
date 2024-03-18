# 321123
def print_fun(n, end="") :
    if n == 0 :
        return
    else :
        print(n, end="")
        print_fun(n-1)
        print(n, end="")
print_fun(3)
print()

# supposed to be 1321121
def print_fun1(n, end="") :
    if n == 0 :
        return
    else :
        print(n, end="")
        print_fun1(n-1)
        print_fun1(n-1)
print_fun1(3)
print()
