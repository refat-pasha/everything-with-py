# Problem 1:

from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def get_balance(self):
        pass
class SavingAccount(BankAccount):
    def __init__(self, dep_bal, with_bal ):
        self.dep_bal = dep_bal
        self.with_bal = with_bal
        self.bal = 0
        self.deposit()
        self.withdraw()

    def deposit(self):
        if self.dep_bal > 0:
            self.bal += self.dep_bal

    def withdraw(self):
        if self.with_bal > self.bal:
            print("Insufficient Balance")
        else:
            self.bal -= self.with_bal

    def get_balance(self):
        print(f"Balance after Deposit: {self.dep_bal}\n"
              f"Balance after Withdraw: {self.with_bal}\n"
              f"Current Balance: {self.bal}")



obj = SavingAccount(2000,200)
obj.get_balance()


