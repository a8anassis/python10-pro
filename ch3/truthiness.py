"""Truthiness in Python."""

FALSE_VALUES = (None, 0, 0.0, "", (), [], {}, set())
TRUTHY_VALUES = (True, 1, -1, 0.1, "Hello", " ", [1], {1}, {1: 'one'})


def main() -> None:
    print("Falsy values:")
    for value in FALSE_VALUES:
        print(f"  {str(value)!r}: {bool(value)}")

    print("\nTruthy values:")
    for value in TRUTHY_VALUES:
        print(f"  {value!r}: {bool(value)}")


if __name__ == "__main__":
    main()