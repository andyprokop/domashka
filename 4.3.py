#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3]
import random

lst = []
for i in range(random.randint(3, 10)):
    lst.append(random.randint(1,200))
print(lst)
new_lst1 = lst[0]
new_lst2 = lst[2]
new_lst3 = lst[-2]
print(new_lst1)
print(new_lst2)
print(new_lst3)
result = [new_lst1, new_lst2, new_lst3]
print(result)