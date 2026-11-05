"""Convert kilograms to grams."""


GRAMS_PER_KILO = 1000

def main() -> None:
    """Διαβάζει έναν αριθμό κιλών από τον χρήστη και εκτυπώνει τον αντίστοιχο αριθμό γραμμαρίων."""

    # Data input
    kilos = int(input("Εισάγετε τον αριθμό των κιλών: "))

    # Processing: Μετατροπή κιλών σε γραμμάρια
    grams = kilos * GRAMS_PER_KILO

    # Εκτύπωση αποτελεσμάτων
    print(f"{kilos} κιλά ισοδυναμούν με {grams} γραμμάρια.")

if __name__ == "__main__":
    main()