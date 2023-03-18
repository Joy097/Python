#----------bubble sort-----------
a=[49 ,39 ,-1 ,-12 ,-16 ,96 ,5 ,78 ,14 ,-15]
print(len(a))
for i in range (len(a)): 
    print (i)# OPTIONAL to understand the range in for loop
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)