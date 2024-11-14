x = int(input('Type password: '))
a = x//10000
two = (x % 10000) // 1000
three = (x % 1000) // 100
four = (x % 100) // 10
five = x % 10

print(five,four,three,two,a)