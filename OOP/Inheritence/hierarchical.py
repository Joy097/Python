class father:
    def __init__(self, name, age):
        self.fname = name
        self.fage = age
        self.fworking= False
    def work(self):
        self.working = True
        
class son1(father):
    def __init__(self, name, age, fname, fage):
        self.name = name
        self.age = age
        self.working= False
        super().__init__(fname,fage)
        
class son2(father):
    def __init__(self, name, age, fname, fage):
        self.name = name
        self.age = age
        self.working= False
        super().__init__(fname,fage)
        
zaber = son1('zaber',34, 'jaker','59')
zaber.work()
print(zaber.fname)