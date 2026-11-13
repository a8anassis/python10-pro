"""Test for Public API της Account class."""

from account import Account
from decimal import Decimal
from exceptions import AccountError

def main() -> None:
    try:
        account = Account(1, "GR12345678901234567890", "John", "Doe", "123-45-6789", Decimal("1000.00"))
        print(account)

        account.deposit(Decimal("500.00"))
        print(f"After deposit: {account}")

        account.withdraw(Decimal("200.00"), "123-45-6789")
        print(f"After withdrawal: {account}")

        # Attempt to withdraw with incorrect SSN
        account.withdraw(Decimal("100.00"), "987-65-4321")

    except AccountError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

