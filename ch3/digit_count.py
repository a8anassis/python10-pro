"""Υπολογισμός του αριθμού των ψηφίων ενός αριθμού."""


def count_digits(n: int) -> int:
    """Υπολογισμός του αριθμού των ψηφίων ενός αριθμού."""
    tmp = abs(n)
    digits = 0

    while True:
        digits += 1
        tmp //= 10
        if tmp == 0:
            break

    return digits

    # return len(str(abs(n)))


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    num = int(input("Εισάγετε έναν ακέραιο αριθμό: "))
    print(f"Ο αριθμός των ψηφίων του {num} είναι: {count_digits(num)}")


if __name__ == "__main__":
    main()