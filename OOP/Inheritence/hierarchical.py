class father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.work= False
    def work(self):
        self.working = True
        
class son1(father):
    def __init__(self, name, age, fname, fage):
        self.name = name
        self.age = age
        self.working= False
        super().__init__()
class son2(father):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.working= False
        
zaber = son1('zaber',34)
zaber.work()
print(zaber.working)