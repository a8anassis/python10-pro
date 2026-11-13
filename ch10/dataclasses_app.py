"""Data classes με τον decorator @dataclass."""

from dataclasses import dataclass


@dataclass
class Point:
    """A point in 2D space."""
    x: int = 0
    y: int = 0


def main() -> None:
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    print(f"Point 1: {p1}")     # str(p1) καλεί την __repr__ μέθοδο
    print(f"Point 2: {p2}")
    print(f"Point 3: {p3}")

    print(f"p1 == p2: {p1 == p2}")  # __eq__ method is automatically generated
    print(f"p1 == p3: {p1 == p3}")

if __name__ == "__main__":
    main()