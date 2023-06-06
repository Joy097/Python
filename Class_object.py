class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def __repr__(self):
        return f'This is a {self.brand}. The model is {self.model} of {self.year}.'
    
car1 = Car('Toyota','Corola','2012')
print(car1)