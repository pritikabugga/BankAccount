from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self, years=1):
        interest = self.current_balance * ((1 + (self.interest_rate / 100)) ** years - 1)
        self.current_balance += interest
        print(f"Interest applied for {years} year(s): ${interest}. New Balance: ${self.current_balance}.")
