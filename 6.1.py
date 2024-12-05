#"a-c" -> abc
#"a-a" -> a
#"s-H" -> stuvwxyzABCDEFGH
#"a-A" -> abcdefghijklmnopqrstuvwxyzA

#first = input("Please enter a letter: ")
#second = input("Please enter another letter: ")
#count = ord(first)
#while count <= ord(second):
   # print(chr(count),end='')
   # count = count + 1

import string

x = string.ascii_letters
#print(x)
inp = input("please type: ")

y,z = inp.split('-')
first_index = x.index(y)
second_index = x.index(z)

result = ''.join(x[first_index:second_index + 1])
print(result)