class BankAccount:
    def __init__(self, odate, balance, withdraw,deposit):
        self.balance = balance
        self.odate = odate
        self.withdraw = withdraw
        self.deposit = deposit

    def getBalance(self):
        result = int(self.balance) + int(self.deposit)
        return result
    
    def __repr__(self):
        return f'''Your account was oopened on {self.odate}. 
Your last withdraw amount is {self.withdraw} Taka.
You deposited amount {self.deposit} Taka.
Your current balance is {self.getBalance()}'''
    
customer1 = BankAccount("2/4/2022", 2000000, 400000, 1000000)
print(customer1)