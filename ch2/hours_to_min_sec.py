"""Convert hours to minutes and seconds."""

MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60


def main() -> None:
    """Διαβάζει έναν αριθμό ωρών από τον χρήστη και εκτυπώνει τον αντίστοιχο αριθμό λεπτών και δευτερολέπτων."""

    # Data input
    hours = int(input("Εισάγετε τον αριθμό των ωρών: "))

    # Processing: Μετατροπή ωρών σε λεπτά και δευτερόλεπτα
    minutes = hours * MINUTES_PER_HOUR
    seconds = minutes * SECONDS_PER_MINUTE

    # Εκτύπωση αποτελεσμάτων
    print(f"{hours} ώρες ισοδυναμούν με {minutes} λεπτά ή {seconds} δευτερόλεπτα.")

if __name__ == "__main__":
    main()

    