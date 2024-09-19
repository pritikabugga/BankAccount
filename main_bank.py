from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

def main():
    # Create accounts
    saving_acc1 = SavingsAccount("Chris", 2500, 300, "112233", "987654", 2)
    saving_acc2 = SavingsAccount("Anna", 3500, 400, "445566", "123456", 4)

    checking_acc1 = CheckingAccount("James", 1000, 150, "778899", "654321", 500)
    checking_acc2 = CheckingAccount("Lily", 2000, 250, "556677", "321654", 1000)

    # Scenario: Savings accounts earning interest and checking accounts making transfers
    print("\n--- Savings Account 1 ---")
    saving_acc1.print_customer_information()
    saving_acc1.apply_interest(2)

    print("\n--- Checking Account 1 ---")
    checking_acc1.print_customer_information()
    checking_acc1.transfer(300, checking_acc2)  # Transfer from checking_acc1 to checking_acc2

    # Scenario for second accounts
    print("\n--- Savings Account 2 ---")
    saving_acc2.print_customer_information()
    saving_acc2.apply_interest(1)

    print("\n--- Checking Account 2 ---")
    checking_acc2.print_customer_information()
    checking_acc2.transfer(700, checking_acc1)  # Transfer from checking_acc2 to checking_acc1

if __name__ == "__main__":
    main()
