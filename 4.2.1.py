l = [1, 3, 5]

if l == []:
    print (0)
else:
    new_l = l[::2]
    y = sum(new_l)
    v = y * (new_l[-1])
    print(v)