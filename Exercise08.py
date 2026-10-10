# statics method vs instance method  and protected method vs private method

class BankAccount:
    min_balance = 100
    
    def __init__(self,owner,balance = 0):          
        self.owner = owner
        self._balance  = balance
        
    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transactions("deposite",amount)
        else:
            print("Deposite amount must be positive.")
    
    def _is_valid_amount(self,amount): # protected method
        return amount > 0 
    
    def __log_transactions(self,transaction_type,amount):  # private method
        print(f"Logging {transaction_type} of ${amount} . new balance: ${self._balance}")
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("kamal",500)
account.deposit(200)

account._is_valid_amount(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))

