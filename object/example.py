class Car:
    def __init__(self, name,type, model, mileage, price):
        self.name = name
        self.type = type
        self.model = model
        self.mileage =mileage
        self.price = price
        
        

car1 = Car("toyota","sedan","allion f15","10","1500000")
print(car1.__dict__)