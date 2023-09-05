x=int(input('give 1st number : '))
y=int(input('give 2nd number : '))
it_is_sunny =True


if(x>y):
    print(x,' is greater than ',y,sep='***')

elif (y>x):
    print( y,' is greater than', x,sep='___')
else:
    print(x, 'and', y ,'are equal',sep='...')

#here the comma uses space automatically. but I am using sep
#to replace the white space with something else

if (it_is_sunny) :
    print ('I will play cricket')
else :
    print('I will go home')

#Not ending the line for every print
print('kire ',end='')
print('vaia ',end=',')
print('kemon ',end='!')