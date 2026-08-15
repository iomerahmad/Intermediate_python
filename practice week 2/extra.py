class BankAccount:
    def __init__(self, name: str, balance: float):
        self.name = name
        self._balance = balance

    @property
    def balance(self)-> float:
        return self._balance

    def __eq__(self, other)-> bool:
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.name == other.name and self._balance == other._balance

    def __repr__(self)-> str:
        return f"Name={self.name!r}, Balance={self._balance}"

    def withdraw(self, amount: float)-> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._balance < amount:
            raise ValueError("Insufficient balance!")
        self._balance -= amount

    def deposit(self, amount: float)-> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def transfer(self, other: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        try:
            other.deposit(amount)
        except:
            ValueError(self.deposit(amount))
            raise
       

