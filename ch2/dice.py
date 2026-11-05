"""Simulate rolling a six-sided die."""

import random

DIE_MIN = 1
DIE_MAX = 6

def main() -> None:
    """"Ρίχνει 2 ζάρια 5 φορές και εκτυπώνει τα αποτελέσματα."""
    for i in range(5):
        die1 = random.randint(DIE_MIN, DIE_MAX)
        die2 = random.randint(DIE_MIN, DIE_MAX)
        print(f"{die1}, {die2}")

if __name__ == "__main__":
    main()