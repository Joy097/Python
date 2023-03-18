'''
a = ()#a empty tuple
b=("mouse",21,[3,4,6],(7,8,9))#different data types
tp=3,4.5,'cat' #tuple packing
a,b,c =tp #tuple unpacking
print(a)
print(b)
print(c)

#indexing
tuple=('a','b',3,4,5)
print(tuple[0],',',end='')
print(tuple[3])
ver=("mouse",21,[3,4,6],(7,8,9))
print(ver[0][2])#u[2] of 'mouse'[0]
print(ver[2][2])
print(ver[3][2])

#if we put list in tuple, then we can change that list
#but tuple is not mutable
er=(1,2,[3,4,5])
er[2][0]=9
print(er)
# can not delete a single item of a tuple 
# but can delete the whole tuple                       
del er
#tuples can be concatenated
print((1,2,3)+(4,5,6))

# so, the advantage of tuple is , it is immutable and 
# can not be changed
'''
#converting list into a tuple
values = input("Input some comma seprated numbers : ")
list = values.split(",")
t = tuple(list)
print('List : ',list)
print('Tuple : ',t)
#hash is only for immutable data types
#hash is like an encoding to check for he correct type of data of file
print(hash(t))
