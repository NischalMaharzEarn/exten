# List
any = ['apple' , 1 , 22.7, 'banana']
print(any)
any.append('cherry')
print(any)
any.insert(1,'pineapple')
print(any)
any.pop(3)
print(any)
any.reverse()
print(any)
del any

l1 = [2,5,6]
l2 = [6,8,9]

l1 = l2
print(l1)
print(l2)

l3 = [5,9,20]
l4 = [10,15,16]

l3 = l4.copy()
print(l4)
print(l3)

#Tuple
car = ('t',5)
print(car)
# immutable

#set no dublicate element and no slicing 
e = {1,2,3,'sd',5}
f = {10,11,12}
print(e.difference(f))
e.add('sjo')
print(e)
