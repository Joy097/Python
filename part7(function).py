#function is a block of code which runs when it is called
#function parts - 
# name 
# parameter list 
# body 
# return 
# 
# 4 types of function -
#(a) built-in (that we already use. ex- print,min,input)
#(b) user-defined(2 types 1.void(return) 2.fruitful(dont return))
#(c) lambda
#(d) recursive     
#-------------------------------------------------------
#USER-DEFINED
from pyexpat import model
from re import A, X


def First_function():
    print("first function is created")
#calling that function
First_function()

#function parts
def funct(x,y):   # x,y are parameters
    max=None      # funct is the function name
    if x>y:       # body is from 25-32 line
        max=x     # returns max
    elif y>x:
        max=y
    else:
        max="both equal"
    return max
print(funct(3,6)) # here 3,6 are arguments

#number of arguments and parameters must be same

#for unknown arguments -
def children(*kids): 
    i=1  # *kids is used for unknown number of arguments
    for x in kids:
        print("child no",i," is",x)  # *kids act like tuple
        i+=1  

children('abir','abid','jony')

#we can also do -
def altr(a,b,c):
    print("okay",a+b+c)

altr(a='succ',c='ful',b='ess')

#for unknown number
def car_(**a):
    print('i want :',a['name'],a['model'])

car_(name='lamborghini',model='avantador')

#if a value is not given the,(NSQUARE example)
def nsquare(x,y=2):    #here y's default value is 2
    return (x*x+2*x*y+y*y)

print('the sum and square of 2 and 2 is :',nsquare(2))
print('the sum and square of 2 and 5 is :',nsquare(2,5))

#Return and Print
def retrn(x):
    return 5*x
print ('first value returns',retrn(2))
print ('second value returns',retrn(8))

#pass statement to pass

def not_complete(s):
    pass
not_complete(1) #so, will not give error

#so, function is a block of code to run multiple times 

#Function - Variable Scoping (local, global, nonlocal)

a='global a'

def funct_1():
    a='ami vaat khai'   #this "a" is a local variable 
    print(a)
funct_1()

#to use the global a also in the function -
def funct_2():
    global a
    print(a)
funct_2()

#Nested function
def outer_f():
    a = "outer a"   # deleting this will print 2x'global a'
    def inner_f():
        a='inner a' # deleting this will print 'outer a'
        print(a)    # prints inner a
    inner_f()
    print(a)        # prints outer a
outer_f()
print(a)            # prints global a

def outer_f():
    a = "outer a"   # Deleting this will print 2x'global a'
                    # We can use the global 'a' 
                    # if we delete this 'a' 
    def inner_f():
        nonlocal a  # This a is the 'outer a' 
        a=a+'ab'    # inner 'a' is deleted
        print(a)    # prints 'inner a'
    inner_f()
    print(a)        # prints 'outer a'
outer_f()
print(a)            # prints 'global a'