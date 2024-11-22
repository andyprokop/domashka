from yaml import YAMLObject

x = input(str('Do you want to continue? Print y/n: '))
while x == 'y':
    a = int(input("Type first figure: "))
    c = input("Select needed action (+, -, *, /): ")
    b = int(input("Type second figure: "))
    if c == '+':
       print(a+b)
       x = input(str('Do you want to continue? Print y/n: '))

    elif c == '-':
       print(a-b)
       x = input(str('Do you want to continue? Print y/n: '))

    elif c == '*':
       print(a*b)
       x = input(str('Do you want to continue? Print y/n: '))

    elif c == '/' and  b != 0:
       print(a/b)
       x = input(str('Do you want to continue? Print y/n: '))

    elif c == '/' and  b == 0:
        print("Try numbers that are not equal to zero")
        x = input(str('Do you want to continue? Print y/n: '))

    else:
        break


