# two parent one child

class engine:
    def __init__(self, name,type, model):
        self.ename = name
        self.etype = type
        self.emodel = model

class bodyKit:
    def __init__(self, spoiler, wheel):
        self.spoiler = spoiler
        self.wheel = wheel
      
        
class Car(engine,bodyKit):
    def __init__(self, ename,etype, emodel, spoiler, wheel):
        engine.__init__(self, ename, etype, emodel)
        bodyKit.__init__(self, spoiler, wheel)
        
    def __repr__(self):
        return f'''This is a {self.ename}. Model is {self.emodel} and it is a {self.etype}.
There is {self.spoiler} Spoiler with {self.wheel} Wheel.'''
        

car1 = Car("V8","v-type","cg18","APEXI","KONING")
print(car1)