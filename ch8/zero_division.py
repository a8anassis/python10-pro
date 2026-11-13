"""Χειρίζεται την εξαίρεση ZeroDivisionError.
DEBUG, INFO, WARNING, ERROR, CRITICAL

"""

import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)

def div(a: int, b: int) -> int | None:
    """Διαιρεί το a με το b.

    Args:
        a (int): Ο αριθμητής.
        b (int): Ο παρονομαστής.

    Returns:
        int | None: Το αποτέλεσμα της διαίρεσης ή None αν ο παρονομαστής είναι μηδέν.
    """
    try:
        return a // b
    except ZeroDivisionError as error:
        logger.error(f"Σφάλμα: Δεν μπορεί να γίνει διαίρεση με το μηδέν. Λεπτομέρειες: {error}")
        raise

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    a = 10
    b = 0

    try:
        result = div(a, b)
        print(f"Το αποτέλεσμα της διαίρεσης {a} // {b} είναι: {result}")
    except ZeroDivisionError:
        print("Σφάλμα: Δεν μπορεί να γίνει διαίρεση με το μηδέν.")
    # else:
    #     print(f"Το αποτέλεσμα της διαίρεσης {a} // {b} είναι: {result}")

if __name__ == "__main__":
    main()