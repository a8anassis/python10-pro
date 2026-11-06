"""Βασική χρήση της προτάσεως match."""


def describe_digit(digit: int) -> str:
    """Περιγράφει έναν αριθμό από 0 έως 9."""
    match digit:
        case 0:
            return "Μηδέν"
        case 1:
            return "Ένα"
        case 2:
            return "Δύο"
        case 3:
            return "Τρία"
        case 4:
            return "Τέσσερα"
        case 5:
            return "Πέντε"
        case 6:
            return "Έξι"
        case 7:
            return "Επτά"
        case 8:
            return "Οκτώ"
        case 9:
            return "Εννέα"
        case _:
            return "Μη έγκυρος αριθμός"


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    for digit in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        description = describe_digit(digit)
        print(f"Ο αριθμός {digit} περιγράφεται ως: {description}")


if __name__ == "__main__":
    main()