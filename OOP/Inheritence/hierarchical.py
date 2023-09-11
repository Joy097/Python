class father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.working= False
    def work(self):
        self.working = True
        
class son1(father):
    def __init__(self, name, age, fname, fage):
        self.name = name
        self.age = age
        self.working= False
        super().__init__(fname,fage)
        self.fname = father.name
        
class son2(father):
    def __init__(self, name, age, fname, fage):
        self.name = name
        self.age = age
        self.working= False
        super().__init__(fname,fage)
        self.fname = father.name
        
zaber = son1('zaber',34, 'jaker','59')
zaber.work()
print(zaber.fname)