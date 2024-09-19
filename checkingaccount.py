from bankaccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient_account):
        if amount > self.transfer_limit:
            print(f"Transfer failed. Amount exceeds limit of ${self.transfer_limit}.")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Transfer failed. Insufficient balance for transfer of ${amount}.")
        else:
            self.current_balance -= amount
            recipient_account.current_balance += amount
            print(f"Transferred ${amount} to {recipient_account.customer_name}. New Balance: ${self.current_balance}.")
