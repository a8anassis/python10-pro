"""Εμφάνιση 10 αστεριών στο τερματικό"""

STARS = 10


def main() -> None:
    """Εμφανίζει 10 αστεράκια στο τερματικό."""
    i = 1
    while i <= STARS:
        print("*", end="")
        i += 1
    print()  # Εκτύπωση νέας γραμμής μετά τα αστεράκια

    # Reverse order
    j = STARS
    while j >= 1:
        print("*", end="")
        j -= 1
    print()  # Εκτύπωση νέας γραμμής μετά τα αστεράκια


if __name__ == "__main__":
    main()