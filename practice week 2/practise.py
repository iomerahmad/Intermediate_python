class BankError(Exception):
    """Base exception for all banking operations."""
    pass

class NegativeDepositError(BankError):
    def __init__(self, amount_deposited: float):
        self.amount_deposited = amount_deposited
        message = f"deposit amount: {amount_deposited} must be positive!"
        super().__init__(message)

def deposit(balance: float, amount: float) -> float:
    if amount > 0:
        return balance + amount
    else:
        raise NegativeDepositError(amount)

try: 
    new_balance = deposit(100, 10)
    print(f"Deposit successful, new balance is: {new_balance}")
except NegativeDepositError as e:
    print(f"Failed: {e}")
    