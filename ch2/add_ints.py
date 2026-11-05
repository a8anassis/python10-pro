"""Add two integers."""


def main() -> None:
    """Διαβάζει δύο ακέραιους από τον χρήστη, τους προσθέτει και εκτυπώνει το αποτέλεσμα."""

    # Data input
    num1 = int(input("Εισάγετε ένα ακέραιο: "))
    num2 = int(input("Εισάγετε έναν δεύτερο ακέραιο: "))

    # Processing: Εκτέλεση πρόσθεσης
    result = num1 + num2

    # Εκτυπώνουμε το αποτέλεσμα
    print(f"Το άθροισμα των {num1} και {num2} είναι: {result}")


if __name__ == "__main__":
    main()