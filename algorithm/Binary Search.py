file1=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')
a=[]
#please dont put any spaces after or before a line in the pyy.txt file

for l in file1 :   
    temp=l.split(' ')
    for i in range (len(temp)):
        a.append(int(temp[i].strip()))

file1.close()  # closing the file is a good practise

q = 0
def binary_search(arr, low, high, x):
 

    if high >= low:
 
        mid = (high + low) // 2
 

        if arr[mid] == x:
            return mid
 
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
    
        return -1

a=sorted(a)
x = int(input("Which number do you wanna search ?"))


result = binary_search(a, 0, len(a)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")


            