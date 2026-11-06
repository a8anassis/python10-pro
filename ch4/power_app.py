"""Υπολογισμός της δύναμης ενός αριθμού."""


def power(base: int, exponent: int) -> int:
    """Υπολογίζει τη δύναμη ενός αριθμού. """
    result = 1

    for _ in range(exponent):
        result *= base

    return result


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    for base, exponent in ((2, 3), (3, 4), (5, 2)):             # unpack tuples

        result = power(base, exponent)

        print(f"{base} ** {exponent} = {result}")


if __name__ == "__main__":
    main()