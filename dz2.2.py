x = int(input('Type password: '))
a = x//10000
two = (x % 10000) // 1000
three = (x % 1000) // 100
four = (x % 100) // 10
five = x % 10
reversed_num = five*10000 + four*1000 + three*100 + two* 10 + a
print(reversed_num)