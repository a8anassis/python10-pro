"""Java varargs in Python"""

def total(*numbers: float) -> float:
    """Υπολογίζει το άθροισμα όλων των αριθμών. Το numbers είναι tuple"""
    return sum(numbers)

def main() -> None:
    print(total(1, 2, 3, 4, 5))  # Output: 15
    print(total(10.5, 20.3, 30.2))  # Output: 61.0
    print(total())  # Output: 0

    nums = [1, 2, 3]
    print(total(*nums))  # Output: 6


if __name__ == "__main__":
    main()