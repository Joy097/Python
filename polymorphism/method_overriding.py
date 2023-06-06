class parent:
    def display(self):
        print("this is parent")
        
class child(parent):
    def display(self):
        print("this is child")
        
parent1 = parent()
child1=child()
parent1.display()
child1.display()

# here, both display method of parent and child class are overridden
# so, overriding happens in parent and chld class and 
# the NAME AND PARAMETER have to be same
