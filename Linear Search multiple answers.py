file1=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')
a=[]
#please dont put any spaces after or before a line in the pyy.txt file

for l in file1 :   
    temp=l.split(' ')
    for i in range (len(temp)):
        a.append(int(temp[i].strip()))

file1.close()  # closing the file is a good practise




def linearSearch(array, n, x):

    r=[]
    for i in range(0, n):
        if (array[i] == x):
            r.append(i)
    return r


x = int(input("Which number do you wanna search ?"))
n = len(a)
result = linearSearch(a, n, x)
if(len(result) == 0):
    print("Element not found")
else:
    print("Element found at index: ",end='')
    for i in result:
      print(i," ",end='')