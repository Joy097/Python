class Animal:
    def sleep(self):
        return "Animal sleep using a support."
    def eat(self):
        return "Animal eat to live."
    def height(self):
        return "Animal height varies a lot."
        
    def __repr__(self):
        return f"{self.sleep()} {self.eat()} {self.height()}"
        
   
        
class Dog(Animal):
    def sleep(self):
        return "Dog sleep by both sitting and laying down."

class Horse(Animal):
    def sleep(self):
        return "Horse sleep by standing."

class Snakes(Animal):
    def sleep(self):
        return "Snakes sleep by laying down."
        
dog1 = Dog()
horse1 = Horse()
snake1 = Snakes()
print(f"""{dog1} 
{horse1} 
{snake1}""")
