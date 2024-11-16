list = [1, 2, 3, 4, 5, 6]
len(list)
x = len(list) // 2
y = len(list) % 2
first_list = list[0:x+y]
second_list = list[x+y:len(list)]
result = [first_list] + [second_list]
print(result)


#=> [[1, 2, 3], [4, 5, 6]]
#[1, 2, 3] #=> [[1, 2], [3]]
#[1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#[1] #=> [[1], []]
#[] #=> [[], []]
