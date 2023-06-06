# method overloading do not have to be in the parent child
# method overloading is SAME NAME DIFFERENT PARAMETER OR PARAMETER TYPE

class OverloadingExample:
   def add(self,a,b):
       print(a+b)
   def add(self,a,b,c):
       print(a+b+c)
       
a=OverloadingExample()
a.add(5,10)
a.add(5,10,20)

# This Gives error because PYTHON DONOT SUPPORT OVERLOADING 
# because python calls only it's latest defined method. ex = def add(self,a,b,c)
