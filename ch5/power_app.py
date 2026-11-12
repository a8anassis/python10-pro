"""Υπολογισμός δύναμης αριθμού."""


def power(base: int, exponent: int) -> int:
    """Επιστρέφει το αποτέλεσμα της δύναμης base^exponent."""
    # return base ** exponent
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    base = int(input("Εισάγετε τη βάση: "))
    exponent = int(input("Εισάγετε τον εκθέτη: "))

    result = power(base, exponent)

    print(f"Το αποτέλεσμα του {base}^{exponent} είναι: {result}")


if __name__ == "__main__":
    main()