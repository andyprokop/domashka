#l = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
#l = [0] #-> [0]
#l = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0] (!!!)
l = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
new_l = []
zeros = []
for i in range(len(l)):
    if l[i] != 0 and i < len(l):
        new_l.append(l[i])
    else:
        zeros.append(l[i])

print(new_l)
print(zeros)
lst = new_l + zeros
print(lst)
