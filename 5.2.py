from yaml import YAMLObject

x = 'y'

while x == 'y':
    a = int(input("Type first figure: "))
    c = input("Select needed action (+, -, *, /): ")
    b = int(input("Type second figure: "))
    if c == '+':
       print(a+b)

    elif c == '-':
       print(a-b)

    elif c == '*':
       print(a*b)

    elif c == '/' and  b != 0:
       print(a/b)

    elif c == '/' and  b == 0:
        print("Try numbers that are not equal to zero")


    else:
        break
    x = input(str('Do you want to continue? Print y/n: '))

