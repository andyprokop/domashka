l = [6]
#[1, 3, 5] => 30
#[6] => 36
#[] => 0
if l == []:
    print (0)
else:
    new_l = []
    x = 0

    for i in l:
        if x % 2 == 0:
            new_l.append(i)
        x += 1
        y = sum(new_l)
        v = y * (new_l[-1])
    print(v)


    #elif l[i] < 0:
      #  print([])
    #elif l[i] == 0:
      #  print(i*i)


#l = [6] #=> 36
#[] #=> 0
#for i in l:
    #if i // 2
