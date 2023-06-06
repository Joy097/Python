#one parent one child
class Car:
    def __init__(self, name,type, model):
        self.name = name
        self.type = type
        self.model = model
    
    def __repr__(self):
        return f'This is a {self.name}. Model is {self.model} and it is a {self.type}.'
        
        
class Vehicle(Car):
    def __init__(self, name,type, model, mileage, price):
        super().__init__(name, type, model)
        self.mileage = mileage
        self.price = price
    
    def __repr__(self):
        return f'''This is a {self.name}. Model is {self.model} and it is a {self.type}.
The mileage is {self.mileage} and price is {self.price}.'''
        

car1 = Vehicle("toyota","sedan","Allion f15","10","1500000")
print(car1)