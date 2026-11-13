"""Defines the Account class and its methods for managing user accounts."""

from decimal import Decimal
from exceptions import InvalidAmountError, InsufficientBalanceError, SsnMismatchError


class Account:
    """A class representing a user account."""

    def __init__(self, id: int, iban: str, firstname: str, lastname: str, ssn: str, balance: Decimal) -> None:
        """Initialize the account with id, iban, firstname, lastname, ssn, and balance."""
        self.id = id
        self.iban = iban
        self.firstname = firstname
        self.lastname = lastname
        self.ssn = ssn
        self.balance = balance

    def deposit(self, amount: Decimal) -> None:
        """Deposit a specified amount into the account."""
        try:
            if amount <= 0:
                raise InvalidAmountError("Deposit amount must be positive.")
            self.balance += amount
        except InvalidAmountError as e:
            print(f"Error: {e}")
            raise

    def withdraw(self, amount: Decimal, ssn: str) -> None:
        """Withdraw a specified amount from the account."""
        try:
            if amount <= 0:
                raise InvalidAmountError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance for the withdrawal.")
            if not self.is_ssn_valid(ssn):
                raise SsnMismatchError("SSN does not match the account holder's SSN.")
            self.balance -= amount
        except (InvalidAmountError, InsufficientBalanceError, SsnMismatchError) as e:
            print(f"Error: {e}")
            raise

    def is_ssn_valid(self, ssn: str) -> bool:
        """Check if the provided SSN matches the account holder's SSN."""
        return self.ssn == ssn

    def __str__(self) -> str:
        return (f"Account(id={self.id}, iban='{self.iban}', "
                f"firstname='{self.firstname}', lastname='{self.lastname}', "
                f"ssn='{self.ssn}', balance={self.balance})")