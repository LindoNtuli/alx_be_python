class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulation using protected member

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

