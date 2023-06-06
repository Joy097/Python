# one child of each father
class Life:
    def __init__(self,name):
        self.lifeName= name
        print(f"This is a {self.lifeName}")
        
    def breathe(self, value):
        print("Does that brethe?: "+value)
        
        
class Animal(Life):
    def __init__(self, aname):
        self.animal = aname
        print(f"The animal is {self.animal}")
        
    def aniChar(self, legs, hands):
        self.legs= legs
        self.hands= hands
        print(f"It has {self.legs} Legs and {self.hands} Hands.")
        

class Monkey(Animal):
    def __init__(self, name, aname, legs, hands, lname, breath):
        self.monkey = name
        print(f"The monkey is {self.monkey}")
        Animal.__init__(self,aname)
        self.aniChar(legs, hands)
        Life.__init__(self, lname)
        self.breathe(breath)
        
monkey1 = Monkey("Japanese macaque", "monkey", "2", "2", "primate", "yes")