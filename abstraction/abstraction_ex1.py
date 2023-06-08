from abc import ABC,abstractmethod
 
try:
    class Animal(ABC):
        
    #concrete method
        def sleep(self):
            print("I am going to sleep in a while")
 
        @abstractmethod
        def sound(self):
	        print("This function is for defining the sound by any animal")
         
except:
    print("error is in the parent class")
        
 
try:
    class Snake(Animal):
        def sound(self):
            print("I can hiss")
            
except:
    print("error is in the Snake class")
 
class Dog(Animal):
    def sound(self):
        print("I can bark")
 
class Lion(Animal):
    def sound(self):
        print("I can roar")
       
class Cat(Animal):
    def sound(self):
        print("I can meow")
        
class Rabbit(Animal):
    def sound(self):
        super().sound()
        print("I can squeak")
        
class Deer(Animal):
    def sound(self):
        pass
 
c = Deer()
c.sound()
c.sleep()
 
c = Rabbit()
c.sound()
        
c = Cat()
c.sleep()
c.sound()
 
c = Snake()
c.sound()