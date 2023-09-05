#a single variable can store many value in list
# a list can contain different type of data. 
# list can be stored in a list
# the range on a list is 0 to n-1. n is unlimited

#mixed data types in list. Also like nested list
a_list = [420,4.20,'joss',False,[1,2.43,'ey']]
#indexing is same as string
print(a_list[3])
#print the whole list inside the list
print(a_list[4])
#print list element inside mother list
print(a_list[4][2])
#we cant change a string but we can change a list
b_list = ['ami','ar','tumi']
b_list[0] = 'she'
print(b_list)

#adding to a list :
#use append(value) function to add one item at end
#use extend([values]) function to add several  at end
#use insert(location,value) to add a value to a location
c_list = ['bmw','ferrari','ford']
c_list.append('append audi')
print(c_list)
c_list.extend(['extend added >', 'mustang','mazda'])
print(c_list)
c_list.insert(2,'inserted toyota')
print(c_list)

#delete elements from list
#clear() - remove all items
#remove(value) - remove the first occurance
# pop([index]) - remove the specific index. otherwise 
# remove the last item from the list like popping.
re_list=[1,2,3,3,4,4,5]
re_list.remove(3)
print(re_list)
re_list.pop()
print(re_list)
re_list.pop(3)
print(re_list)
re_list.clear()#make the list blank
print(re_list)

#del also works like pop function
d_list = [0,9,8,7,6,5]
del d_list[2]
print(d_list)
del d_list # delete the list
#print(d_list)

#index(element[start,end]) - to find in start to end index
# index(element) function is used to find the first occurance
v=[1,22,3,4,3,7,5]
print(v.index(22))
print(v.count(3))#count the number of occur
# sort(reverse=True/False) - is used to sort in desceding 
# or ascending order
v.sort()#ascending order
print(v)
v.sort(reverse = True) #descending order
print(v)

#reverse() - used to just reverse the list
r = [2,1,5,8,4]
r.reverse()
print(r)

#adding two list
s=[20,30,40]
print(r+s)
r.extend(s)
print(r) #now list s is in list r

#multiply a list
print(s*3)
#iteration
for x in s:
    print(x)
#check item in the list
print(20 in s)
#slicing here is like string
#list[start:end:step]
slice=['red','blue','yellow','green','purple']
print(slice[:])
print(slice[3:])
print(slice[:3])
print(slice[2:4])
print(slice[::2])
print(len(slice)) #length
num=[1,4,5,2,3]
print(max(num)) #max
print(min(num)) #min
print(sum(num)) #sum

#list copy
vv=num.copy()
print(vv)






