#----------selection sort----------
list = [93 ,-22 ,40 ,-49 ,-12]

for i in range(len(list)):
    min=i
    for j in range(i+1, len(list)):
        if list[min]>list[j]:
            min=j
    temp=list[min]
    list[min]=list[i]
    list[i]=temp
print(list)

