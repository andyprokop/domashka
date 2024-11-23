import keyword
import string
from curses.ascii import islower
words = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

my_string = input(str("type your input: "))
my_string_new = my_string.split("_")
#print(my_string_new)
x = len(my_string_new)
#print(x)

if my_string.islower() != True:
    print ('False')

elif my_string.find('0') == 0 or my_string.find('1') == 0 or my_string.find('2') == 0 or my_string.find('3') == 0 or my_string.find('4') == 0 or my_string.find('5') == 0 or my_string.find('6') == 0 or my_string.find('7') == 0 or my_string.find('8') == 0 or my_string.find('9') == 0:
    print ('False')
elif any(word in words for word in my_string_new) and x <= 1:
    print ('False')
elif my_string.find('_') >= 0:
    print ('True')
elif my_string.isalnum() != True:
    print ('False')
else:
    print ("True")
#print(string.punctuation)

#ind = my_string.find('e')
#ind = my_string.find('e', ind + 1) # Пошук індексу наступного елемента
#print(ind)
#print(my_string.find('e', ind + 1))


#x = my_string.isalnum()#пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_". - done

#починатися з цифри - done
#print(my_string.islower())#містити великі літери - done
#бути жодним із зареєстрованих слів.

#digit = 0
#for s in my_string:
   # if s.isalnum():
      #  digit += 1
       # print(s, end='')
#print(keyword.kwlist)
#print(digit)
