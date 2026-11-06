"""Υπολογισμός της άθροισης των n πρώτων φυσικών αριθμών"""
from ch1.expressions import total


def sum_first_n(n: int) -> int:
    """Υπολογίζει το άθροισμα των n πρώτων φυσικών αριθμών.

    Args:
        n (int): Ο αριθμός των πρώτων φυσικών αριθμών που θα αθροιστούν.

    Returns:
        int: Το άθροισμα των n πρώτων φυσικών αριθμών.
    """
    total_sum = 0
    i = 1

    while i <= n:
        total_sum += i
        i += 1

    return total_sum
    # return n * (n + 1) // 2

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    n = 10
    result = sum_first_n(n)
    print(f"Το άθροισμα των {n} πρώτων φυσικών αριθμών είναι: {result}")