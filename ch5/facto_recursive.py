"""Υπολογισμός παραγοντικού αριθμού με αναδρομή."""


def factorial(n: int) -> int:
    """Υπολογίζει το παραγοντικό ενός αριθμού n με αναδρομή."""
    if n == 0:
        return 1

    return n * factorial(n - 1)


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    num = int(input("Εισάγετε έναν ακέραιο αριθμό: "))

    result = factorial(num)

    print(f"Το παραγοντικό του {num} είναι: {result}")

if __name__ == "__main__":
    main()