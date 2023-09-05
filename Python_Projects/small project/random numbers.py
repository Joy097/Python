import random

#to see all the functions of RANDOM >
print(dir(random))


#let's generate random numbers >
for i in range(10):
    print(random.uniform(3,7)) # generate 10 floats


# USE THESE FUNCTIONS AS random.(the desired function)

# 1. Genrally the "random()" function prints the floating
# values between 0 to 1. if not mentioned 

# 2. Use "randint(low,high)" for integers. high will print

# 3. In "normalvariate(x,y)" ,the x is mean and y is 
# standard deviation. which is used for very small value

# 4. "choice(given list)" - takes random values from the list
# 5. "uniform(low,high)" - gives any float number in the range
# 6. "random()" generate number in 0-1

#RANDOM VALUE FROM THE LIST
list=['rock','paper','scissors']
for i in range(10):
    print(random.choice(list))