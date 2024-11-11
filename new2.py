#user_password = input("Insert password: ")
#password = user_password
#left, right = divmod(user_password, 1000)
#print(left, right)
x = int(input('Type password: '))
one = x // 1000
two = (x % 1000) // 100
three = (x % 100) // 10
four = x % 10
print(one)
print(two)
print(three)
print(four)