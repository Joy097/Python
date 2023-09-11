class father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.work= False
    def work(self):
        self.work = True
        
class son1(father):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.work= False
class son2(father):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.work= False
        
zaber = son1('zaber',34)
print(zaber.father.name)