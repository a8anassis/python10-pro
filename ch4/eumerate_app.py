"""Οι συναρτήσεις enumerate() και zip() στην Python."""

NAMES    = ("Άννα", "Βασίλης", "Γιώργος")
GRADES = (85, 92, 78)


def main() -> None:
    print("Χρήση της enumerate():")
    for index, name in enumerate(NAMES, start=1):
        print(f"  {index}: {name}")

    print("\nΧρήση της zip():")
    for name, grade in zip(NAMES, GRADES, strict=True):
        print(f"  {name}: {grade}")


    total = 0
    for grade in GRADES:
        total += grade
    print(f"\nΜέσος όρος βαθμολογίας: {total / len(GRADES):.2f}")


if __name__ == "__main__":
    main()