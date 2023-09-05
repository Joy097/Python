import string
import random 

lo = string.ascii_lowercase
up = string.ascii_uppercase
dig = string.digits
sym = string.punctuation

str = lo+up+dig+sym
ran_pass = random.sample(str,8) #number of char you want
passd = ''.join(ran_pass)
print(passd)