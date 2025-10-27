class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance                                                    #Store balance.

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance):          #Check if both account is valid.
            return False
        if not self.withdraw(account1, money):                                    #Try to withdraw from account1.
            return False                                                          #If not possible, return false.
        return self.deposit(account2, money)                                      #Return if possible to deposit to account 2.

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):                                           #Check if account is valid.
            return False
        self.balance[account - 1] += money                                        #Deposit money.
        return True                                                               #Return true.

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) or self.balance[account - 1] < money:      #Check if account is valid and has enough balance.
            return False
        self.balance[account - 1] -= money                                        #Withdraw money.
        return True                                                               #Return true.


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
