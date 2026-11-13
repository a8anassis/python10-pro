"""Custom exceptions for the account_app module."""


class AccountError(Exception):
    """Base class for account_app-related exceptions."""

class InvalidAmountError(AccountError):
    """Raised when an invalid amount is provided for a transaction."""

class InsufficientBalanceError(AccountError):
    """Raised when an account_app has insufficient balance for a transaction."""

class SsnMismatchError(AccountError):
    """Raised when there is a mismatch in the provided SSN."""


