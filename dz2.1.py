x = int(input('Type password: '))
one = x // 1000
two = (x % 1000) // 100
three = (x % 100) // 10
four = x % 10
print(one)
print(two)
print(three)
print(four)