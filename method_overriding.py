# same method but in different parent and child class

class parent:
    def call_me():
        print("I'm a parent")

class child(parent):
    def call_me():
        print("I'm a child")
        
parent1 = parent()
child1 = child()

parent.call_me()
child.call_me()