"""Χρήση προτάσεων match με μοτίβα."""

from enum import IntEnum


class Weekday(IntEnum):
    """Αριθμητική αναπαράσταση των ημερών της εβδομάδας."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_weekday_name(day: int) -> str:
    """Επιστρέφει το όνομα της ημέρας της εβδομάδας με βάση τον αριθμό της."""
    match day:
        case Weekday.SATURDAY | Weekday.SUNDAY:
            return "Σαββατοκύριακο"
        case _ if Weekday.MONDAY <= day <= Weekday.FRIDAY:
            return "Εργάσιμη ημέρα"
        case _:
            return "Μη έγκυρη ημέρα"


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    for day in range(1, 7):  # Δοκιμάζουμε από 1 έως 8 για να καλύψουμε και μη έγκυρες ημέρες
        print(f"Η ημέρα {day} είναι: {get_weekday_name(day)}")

if __name__  == "__main__":
    main()