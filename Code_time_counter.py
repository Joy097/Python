import time
import timeit

#give your smart code here
def smart():
        ############CODE###############
    print("a"+"b"+"c")

    ############^^^^CODE^^^^###############
    print("smart : ")

#give your naive code here
def naive():
        #############CODE##############
    a='a'
    b='b'
    c='c'
    print(a,b,c,sep="")
    #############^^^^CODE^^^^##############
    print("naive : ")

# prints the time

print(timeit.timeit('smart()',number=10,globals=globals()))

#this will run the code inside naive for 10 times and give the total time
time.sleep(2) #cooldown for 2 second

print(timeit.timeit('naive()',number=10,globals=globals()))