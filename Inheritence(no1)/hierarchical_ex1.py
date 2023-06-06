#one father many child
class ferrari:
    def __init__(self):
        self.name = 'Ferrari'
        self.country = 'Italy'
    
    def __repr__(self):
        return f'''{self.name} is from {self.country}. 
{self.model} was unvailed at {self.year} '''

class Ferrari_F12(ferrari):
    def __init__(self):
        self.model = "Ferrari F12"
        self.year = "2009"
        super().__init__()
    
class Ferrari_599(ferrari):
    def __init__(self):
        self.model = "Ferrari 599"
        self.year = "2006"
    
class Ferrari_F430(ferrari):
    name = "F430"  
        
ferrari1 = Ferrari_F12()
print(ferrari1)
ferrari2 = Ferrari_F430()
print(ferrari2)
        