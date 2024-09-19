class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
            print(f"{amount}EUR noguldīti kontā.")
        else:
            print("Noguldīšanas summai jābūt pozitīvai.")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Nepietiekami līdzekļi izņemšanai.")
        elif amount<=0:
            print("Izņemšanas summai jābūt pozitīvai .")
        else:
            self.__balance-=amount
            print(f"{amount}EUR izņemti no konta.")
    
account=BankAccount(100)
print("Pašreizējais atlikums : ",account.get_balance())
account.deposit(50)
print("Pašreizējais atlikums pēc noguldījuma:",account.get_balance())
account.withdraw(50)
print("Pašreizējais atlikums pēc izņemšanas:",account.get_balance())
