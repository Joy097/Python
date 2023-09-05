# variable naming convention -
# snake_casing 
# start with no digit , no white space and special signs
#case sensitive
#cant use special words, have to use meaningful name
#---------variables and data types----------
hen = 'chicken'

print(hen)

int = 25
flo = 80.3
str = 'car'
lis = ['apple','banana','cherry']

print(type(lis))

tup = ('I','cant','change','this.','because','this','is','tuple')
print(type(tup))

v=1
z=3

print(type(v<z))

car_dictionary = {
    'brand':'Toyota' ,
    'model':'Supra' ,
    'man_year': 2006,
    'owner':"Joy_Chowdhury",
    'milage':12468+1,
}
print(type(car_dictionary['milage']))

a=12
b=22
c=4
d=10
arithmetic_ops=a+b*c/d

print(arithmetic_ops)
gg="okay then, learnt the very very basics of variable and data type of python."

print(gg)
#----------------Operators----------------
n='arithmetic operation'
a=20
b=33
c=11
d=22
e=7
f=11

add=a+b
sub=e-f
mul=d*a
exp=c**e
mod=d%f
e/=4


print(add,sub,mul,exp,mod)

#floor division
print(5//2)
print(-5//2)
#identity opt
print(c is f)
print(c is not f)
print(c is d)
#python membership operator
v=['ami','tumi','danish']
x='ajaira'
print('i' in x)
print('ami' not in v)


#--------------------input and type convertion------------------------

B=input("Give your number : ")
#input takes string by default. so-
C=int(input("enter the number : "))

C+=200
print(B)
print(C)
#type conversion -
a=int(1.5)
b=float(3)
c=int('123')
c-=2
print(c)
f=str(2)
print(type(f))
print("now go home lad")
