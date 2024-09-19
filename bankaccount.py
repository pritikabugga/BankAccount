class BankAccount:
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected
        self.__routing_number = routing_number  # Private

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.current_balance}.")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Inadequate balance. Cannot withdraw ${amount}.")
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.current_balance}.")

    def print_customer_information(self):
        print(f"Customer: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
