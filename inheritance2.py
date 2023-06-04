class Vehicle:
    def __init__(self,name, speed, mileage, seats):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.seat = seats
        
    def getTotalFare(self):
        return int(self.seat) * 100
    def __repr__(self):
        return f'Vehicle Name: {self.name}, Speed: {self.speed}, Mileage: {self.mileage}, Total Fare: {self.getTotalFare()} ' 

class Bus(Vehicle):
    def __init__(self,name, speed,mileage, seats):
        super().__init__(name, speed, mileage, seats)
    
    def getTotalFare(self):
        fare = super().getTotalFare()
        return fare+fare*.1
        
vehicle = Vehicle("Supra","300mph","8 km/h","2")
bus1 = Bus("School Volvo","180","12","20")
print(vehicle)
print(bus1) 
        