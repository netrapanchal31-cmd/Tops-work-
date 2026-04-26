#encapsulation = binding data and method together and it cannot access easily to anyone,,, for privacy we can use _or__
class bank:
    def __init__(self,balance,name):
        self.__balance=balance
        self.name=name
    def deposit(self,amount):
        self.__balance+=amount
        
    def withdraw(self,amount,name):
        if amount >= 5000:
           
            print("you can withdraw only 5000")
            
        else:
            print("withdraw successfully")
           
            self.__balance-=amount
        self.name=name
           
        
    def getbalance(Self):
        return Self.__balance
   
        
    
obj=bank(10000,"Netra")
print(f"{obj.name} Initial balance is {obj.getbalance()}")
obj.withdraw(4000,"netra")

print(f"{obj.name} balance is {obj.getbalance()}")


           
