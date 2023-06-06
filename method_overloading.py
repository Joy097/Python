#Overloading is using method of same names in same class but diff attributes

class Overloading:
    def add(self,x,y):
        print(x+y)
    def add(self,x,y,z):
        print(x+y+z)

obj = Overloading()
obj.add(1,2)

# it will show an error because python remembers only the recent definition of add
