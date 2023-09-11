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
        super().__init__(fname,fage)
class son2(father):
    def __init__(self, name, age, fname, fage):
        self.name = name
        self.age = age
        self.working= False
        super().__init__(fname,fage)
        
zaber = son1('zaber',34, 'jaker')
zaber.work()
print(zaber.working)