#-------------------- SORTING --------------------

#Ascending sort
num1=[6,5,7,2,5,9,0,2,4,1]
num_sort=sorted(num1) 
print('unsorted n1 :',num1)
print('sorted n1 :',num_sort)

print('---------------------------')
#Descending sort
num2=[13 ,10 ,15 ,6 ,2 ,12 ,4 ,7 ,14 ,1]
num_sort2=sorted(num2,reverse=True)

print('unsorted n2 :',num2)
print('sorted n2 :',num_sort2)


print('---------------------------')

#sorting for string 

num3='Amar onek mon kharap'
num_sort3=sorted(num3)

print('unsorted string :',num3)
print('sorted string :',num_sort3)

# *** the list can not be of mixed types (string,int)****

#dictionary sort
inv={'lays':30,'twist':10,'snickers':25,'sun':70}
sort_inv = sorted(inv)
print(sort_inv)
dic={}
for i in sort_inv:
    dic[i]=inv[i]
print(dic)

#directly sort a list
sort2=[8 ,14 ,1 ,8 ,5 ,1 ,15 ,9 ,7 ,10]
sort2.sort()
print(sort2)