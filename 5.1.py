import keyword
import string
from curses.ascii import islower
from sys import excepthook

words = keyword.kwlist
char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`',' ']


my_string = input(str("type your input: "))
my_string_new = my_string.split("_")
#print(my_string_new)
x = len(my_string_new)
#print(x)
if my_string == ('_'):
    print('True')
elif my_string.islower() != True:
    print ('False')

elif my_string.find('0') == 0 or my_string.find('1') == 0 or my_string.find('2') == 0 or my_string.find('3') == 0 or my_string.find('4') == 0 or my_string.find('5') == 0 or my_string.find('6') == 0 or my_string.find('7') == 0 or my_string.find('8') == 0 or my_string.find('9') == 0:
    print ('False')
elif any(word in words for word in my_string_new) and x <= 1:
    print ('False')
elif any(character in char for character in my_string):
    print ('False')
#elif my_string.find('_') >= 0:
 #   print ('True')
#elif my_string.isalnum() != True:
  #  print ('False')
else:
    print ("True")

