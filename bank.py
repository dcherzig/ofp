#%%
from datetime import datetime

#%%
class Account:
    limit=0
    def __init__(self):
        self._balance = 0
        self._transactions =[] #privat machen -> Konsistenz haben

    def get_balance(self): #__get_balance, öffentlich lassen
        return self._balance
    
    def get_transactions(self, n):
        return self._transactions[:n]     

    def cash_deposit(self, amount):
        if amount > 0:
            self._balance += amount
            time = str(datetime.now()) #muss keine Instanzvariable sein, ist eine normale Variable einer Funktion -> nur time nennen
            self._transactions.append([time, amount, self._balance])
        else:
            raise Exception

    def withdraw(self, amount, id_dep):
        self._balance -= amount
        if amount-self._balance >= Account.limit:
            time = str(datetime.now())
            self._transactions.append([time, amount, self._balance, id_dep])
        else:
            raise Exception                       

    def deposit(self, amount, id_with):
        self._balance += amount
        time = str(datetime.now())
        self._transactions.append([time, amount, self._balance, id_with])

class YouthAccount(Account):
    def withdraw(self, amount, id_dep):
        if self._balance - amount >=Account.limit:
            super().withdraw(amount, id_dep)
        else:
            raise Exception

class SavingAccount(Account):
    def withdraw(self, amount, id_dep,):
        FEE = 0.50
        if self._balance - amount >=Account.limit:
            super().withdraw(amount, id_dep)
            self._balance -= FEE
        else:
            raise Exception
    
    def int_rate(self):
        INT_RATE=1.005
        self._balance *= INT_RATE

class PrivateAccount(Account):
    limit=-500
    def withdraw_priv(self, amount, id_dep):        
        if self._balance - amount >= PrivateAccount.limit:
            super().withdraw(amount, id_dep)
        else:
            raise Exception


#%%
class Bank:
    def __init__(self):
        self._accounts = {}
        self._id = 1

    def create_account(self, type):
        if type == "YouthAccount": #elif
            self._id += 1
            self._accounts[self._id]= YouthAccount()
            return self._id 
        elif type == "SavingAccount":
            self._id += 1
            self._accounts[self._id]= SavingAccount()
            return self._id 
        elif type == "PrivateAccount":
            self._id += 1
            self._accounts[self._id]= PrivateAccount()
            return self._id 
        else:
            raise Exception

    def delete_account(self, id):
        if self._accounts[id].check_balance() == 0:
            del self._accounts[self._id]
        else:
            return "Deleting the account is not possible"

    def transaction(self, id_with, id_dep, amount):
        if id_with in self._accounts and id_dep in self._accounts:
            try:
                self._accounts[id_with].withdraw(amount, id_dep)
                self._accounts[id_dep].deposit(amount, id_with)
            except:
                raise Exception
        else:
            return "The account is not available"

    def cash_deposit(self, amount, id):
        try:
            self._accounts[id].cash_deposit(amount)
        except:
            return f"The account is not available"

    def check_balance(self, id):
        try:
            return self._accounts[id].get_balance() #öffentlich!!
        except:
            raise Exception

    def check_transactions(self, id, n):
        try:
            return self._accounts[id].get_transactions(n)
        except:
            raise Exception

#%%
Sarasin = Bank()
Acc_1 = Sarasin.create_account("YouthAccount")
Acc_2 = Sarasin.create_account("PrivateAccount")
Sarasin.cash_deposit(400,Acc_1)
Sarasin.cash_deposit(400,Acc_2)
Sarasin.check_transactions(Acc_1,2)
Sarasin.check_balance(Acc_1)

Sarasin.transaction(Acc_1,Acc_2,200)


#%%
Sarasin.transaction(Acc_1,Acc_2,200)
Sarasin.check_balance(Acc_1)
Sarasin.check_balance(Acc_2)

# %%
Sarasin.check_transactions(Acc_2,5)
# %%
Sarasin.transaction(Acc_2,Acc_1,1000)
Sarasin.check_balance(Acc_2)
# %%
