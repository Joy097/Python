list=input("Give a list: ").split()
dictionary={}
for i in list:
    count=0
    for j in list:
        if i == j:
            count+=1
    found=0
    for k in dictionary:
        if i == k:
            found=1
    
    if found==0:
        dictionary[i]=count

print(dictionary)