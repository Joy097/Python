fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "r" in x]
#this means, newlist items will be x, where for each x in list, it has to
#have an "a" in it

print(newlist)