class GrandFather:
    def __init__(self,name,age, disease):
        self.name = name
        self.age = age
        self.disease = disease
        self.savings = self._getSavings()
        self.girlfriend = self.__getGirl()
        
    def _getSavings(self):     # this is a protected method
        self.savings = int(self.age)*3333
        return self.savings
        
    def __getGirl(self):
        return f"{self.name}a"
        
class Father(GrandFather):
    def __init__(self,name,age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.savings = self._getSavings()
        
        

class Child(Father):
    def __init__(self,name,age, disease):
        GrandFather.__init__(self, name, age, disease) #can access grand parent class
        
childDisease = Child("anam","23","pneumonia")
print (childDisease.disease) #called through accssing grand parent class: GrandFather.__init__

grandfather = GrandFather("jadu","91","heart")
print(grandfather.savings)  # called through protected method: _getSavings(self)
print(grandfather.girlfriend) #called through private method: __getGirl(self)

father = Father("babu","56","120000")
print(father.savings) # called through protected method: _getSavings(self)

#print(childDisease.disease)

