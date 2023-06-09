from abc import ABC, abstractmethod
import datetime

class Account(ABC):
    def __init__(self):
        self.money = 0
        self.opendate = datetime.date.today()
    
    @abstractmethod
    def Deposit(self):
        pass
    @abstractmethod
    def Withdraw(self):
        pass
    @abstractmethod
    def Balance(self):
        pass
    
    
class User(Account):
       
    def Deposit(self,amount):
        self.money += amount
        return f"{amount} tk is deposited"
        
    def Withdraw(self,amount):
        if self.money<amount:
            return "not enough money"
        elif self.money==amount:
            self.money = 0
            return f"{amount} tk is withdrawn"
        else:
            self.money -= amount
            return f"{amount} tk is withdrawn"
            
    def Balance(self):
        return self.money
    
    
user1 = User()

print(user1.Deposit(5000))
print(user1.Deposit(3000))
print(user1.Withdraw(9000))
print(user1.Balance())

user2 = User()

print(user2.Deposit(10000))
print(user2.Withdraw(9000))
print(user2.Deposit(30000))
print(user2.Withdraw(19000))
print(user2.Balance())

# this will give the balance after every month on the account opened day
while True:
    current = datetime.date.today().day
    if current == user1.opendate.day:
        print(f'This month, your balance is {user1.Balance()}tk')
        # on the account open day, it will give the balance once
        while current <= user1.opendate.day:
            pass
    
   