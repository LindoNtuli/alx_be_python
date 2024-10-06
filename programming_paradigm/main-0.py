import sys
from bank_account import BankAccount

def main():
    # Check command line arguments for initial balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <initial_balance>")
        return
    
    try:
        initial_balance = float(sys.argv[1])
    except ValueError:
        print("Invalid initial balance. Please enter a numeric value.")
        return

    account = BankAccount(initial_balance)
    account.display_balance()

if __name__ == "__main__":
    main()
