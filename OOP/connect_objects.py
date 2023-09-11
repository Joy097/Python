class husband:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def marry(self,wife):
        self.wife = wife
        
class wife:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def marry(self,husband):
        self.husband = husband
        
husband1 = husband('joy','26')
wife1 = wife('janvi','25')

print(husband1.name)