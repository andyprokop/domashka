a = int(input("Type first figure: "))
b = int(input("Type second figure: "))
c = input("Select needed action (+, -, *, /): ")
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/' and  b != 0:
    print(a/b)
else:
    print("Try numbers that are not equal to zero")