#'Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string
from os import remove

b = string.punctuation
b = list(string.punctuation)
b.append(" ")
my_string = input(str("type your input: "))
my_string = my_string.title()
for char in b:
    my_string = my_string.replace(char,"")
#my_string_new = my_string_new[0, '#']
#my_string.remove(char)
my_string = my_string[:140]

print('#' + my_string)
