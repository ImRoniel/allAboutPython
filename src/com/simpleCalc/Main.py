from random import choice
from traceback import format_list

#Calculator
print("1. Add")
print("2. Minus")
print("3. Multiplication")
print("4. divide")
print("choose 1")
choice = int(input())
result = 0.0
match choice:
    case 1:
        print("Enter Your First Number:")
        firstminnum = float(input())
        print("Enter seconde number:")
        secaddnum = float(input())
        result = firstminnum + secaddnum
        print(result)
    case 2:
        print("Enter Your First Number:")
        firstminnum = float(input())
        print("Enter seconde number:")
        secminnum = float(input())
        result = firstminnum - secminnum
        print(result)
    case 3:
        print("Enter Your First Number:")
        firstmulnum = float(input())
        print("Enter seconde number:")
        secmulnum = float(input())
        result = firstmulnum + secmulnum
        print(result)
    case 4:
        print("Enter Your First Number:")
        firstdivnum = float(input())
        print("Enter seconde number:")
        secdivnum = float(input())
        result = firstdivnum / secdivnum
        print(result)
    case _:
        print("Invalid You son of a Bitch ")