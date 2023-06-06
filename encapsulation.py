#Encapsulation is preventing the user from accessing certain parts of the code
# As an example, __discount attribute can not be accessed as it is a private class

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

car1=Car('ferrari','entigo56','2017',120)
car1.set_discount(0.30)
print(car1)    