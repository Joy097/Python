
float = 2.1
format_float = "{:.2f}".format(float)
print(format_float)


exit()
#list plus for loops
list=["jorina","sokhina","morjina","rojina"]
print(list[0])
for any_variable in list:

    print(any_variable)

x=[23,94,32,14,77]
sum=0
for i in x:
    sum+=i
print(sum)

largest = -999
for i in x:
    if i>largest:
        largest = i
print(largest)

#for loop using range

for counter in range (2):
    print("ami onek joss",counter)

print('----------')
for counter in range (2,5):
    print("ami onek joss",counter)

print('----------')

for counter in range (2,10,2):
    print("ami onek joss",counter)

sequence = range(0,5,1)
print(sequence[0])
print(sequence[3])
print(sequence[-2])
print(sequence[-4])

print('-----------')
#bubble sorting
bb=[2,3,9,0,6,1,7,87,33,55,33,22,11,55,88,99]
for i in range (len(bb)) :
    for j in range(i,len(bb)):
        if bb[i]<bb[j]:
            temp=bb[i]
            bb[i]=bb[j]
            bb[j]=temp


for i in bb:
    print(i)
print ("list size",len(bb))

#this pass is used when I will continue this code later
w=22
if(w<30):
    pass
print('other lines of the codes')
