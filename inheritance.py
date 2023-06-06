class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self._discount = None
    
    def set_discount(self,discount):
        self._discount = discount
    
    def get_price(self):
        if self._discount:
            return self.price * (1-self._discount)
        return self.price
    
    def __repr__(self):
        return f'This is a {self.brand}. The model is {self.model} of {self.year}. The price is {self.get_price()} million'

class Manufacturer(Car):
    def __init__(self, brand, model, year, price, manufacturer):
        super().__init__(brand, model, year, price)
        self.manufacturer = manufacturer
        
    def __repr__(self):
        return f'This is a {self.brand}. The model is {self.model} of {self.year}. The price is {self.get_price()} million. Manufactured by {self.manufacturer}'
        
class machine(Car):
    def __init__(self, brand, model, year, price, machine):
        super().__init__(brand, model, year, price)
        self.machine=machine
    def __repr__(self):
        return f'This is a {self.brand}. The model is {self.model} of {self.year}. The price is {self.get_price()} million with {self.machine}.'
        
car1=Car('ferrari','entigo56','2017',120)
car1.set_discount(0.30)
print(car1)    

engine = machine('ferrari','friza88','2007',150, 'zotac')
manufacturer=Manufacturer('Toyota','Corola','2012',65,'bangladesh')
print(manufacturer)
print(engine)