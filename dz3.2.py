from numpy.ma.core import append
#lst1 = [12, 3, 4, 10]
#=> [10, 12, 3, 4]
#lst1 = [1] #=> [1]
#lst1 = [] #> []
lst1 = [12, 3, 4, 10, 8]
x = lst1[-1]
lst1.insert(0, x)
del (lst1[-1])
#=> [8, 12, 3, 4, 10]
print(lst1)