"""Data classes manual examples."""


class Point:
    """A point in 2D space."""

    def __init__(self, x: float, y: float) -> None:
        self._x = x     # κατά σύμβαση, private attribute με _
        self._y = y

    def __str__(self)  -> str:
        return f"Point({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Point({self._x!r}, {self._y!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y


def main() -> None:
    p1 = Point(1.0, 2.0)

    print(f"Point 1: {p1}")     # str(p1) καλεί την __str__ μέθοδο


if __name__ == "__main__":
    main()
