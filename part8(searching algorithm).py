#------------ linear search -------------
List=[57 ,23 ,-18 ,86 ,85 ,-25 ,-4 ,47 ,-5 ,93]

def linear_search(L1,x):
    for i in L1:
        if i==x:
            return L1.index(i)
    return -10


index=linear_search(List,86)

if index == -10 :
    print('We didnt found the number')
else:
    print('We found the number at index :',index) 

#----------Binary Search----------
# Binary search = first we have to sort the list
# Then, we have to divide the whole list and 
# search again an again

L2=[3 ,24 ,10 ,-40 ,-1 ,64 ,86 ,6 ,-32 ,64]
L2.sort()
print('sorted list :',L2)
def binary_search(sorted,x):
    #pass
    l=0
    r=len(sorted)-1
    print(r)
    while l<=r:
        mid_i=l+(r)//2
        if sorted[mid_i]==x:
            return mid_i
        elif sorted[mid_i]>x:
            r=mid_i-1
        else:
            l=mid_i+1
        return None

index1=binary_search(L2,64)
if index1==None:
    print('not found')
else:
    print('Found the number in  index :',index1)