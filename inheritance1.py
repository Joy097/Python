class Vehicle:
    def __init__(self,name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        
    def __repr__(self):
        return f'Vehicle Name: {self.name}, Speed: {self.speed}, Mileage: {self.mileage}' 

class Bus(Vehicle):
    def __init__(self,name, speed,mileage):
        super().__init__(name, speed, mileage)
        
bus1 = Bus("School Volvo","180","12")
print(bus1) 
        