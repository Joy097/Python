
#while loop
count=1
while(count<=10):
    x=count
    print('print kor vai',x,'bar')
    count+=1

#printing all the even numbers
count=1
x=int(input('give the limit you want to check : '))
while(count<=x):
    if(count%2==0):
        print(count,' is an even number')
    count+=1

#breaking
var=1
while True:
    print('continue',var)
    var+=1
    if var==12:
        break

#continuing
ben=1
while ben<=5:
    
    if ben>=4:
        continue
    print(ben,' ta babu')
    ben+=1

#nested while
outer =1 
while outer<=3:
    inner =1
    while inner<=3:
        core =1
        while core<=3:

            print(outer,inner,core)
            core+=1
        print('getting out of the core loop')
        inner+=1
    print('getting out of the inner loop')
    outer+=1
print('getting out of the outer loop')