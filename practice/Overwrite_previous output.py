#it works good in the case of a clock
import time

spaces=" "*10
print('\rHey, How are you?',end='')
time.sleep(1)
print('\rI saw you yesterday'+spaces,end='')
time.sleep(1)
print('\rBut I was busy'+spaces,end='')

# '\r' works to go to the previous line 
# (end="") works to remove the line gap of print
# spaces are to minimize the big lines effect(remove it and see result)
