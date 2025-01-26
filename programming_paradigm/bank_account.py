class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance with an optional initial balance.
        Default balance is 0 if not specified.
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        Returns True if the withdrawal is successful, False otherwise.
        """
        if amount > self._account_balance:
            return False
        if amount > 0:
            self._account_balance -= amount
            return True
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")

