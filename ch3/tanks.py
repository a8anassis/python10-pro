"""Εφαρμογή δεξαμενών.

- Πορτοκαλί: μία δεξαμενή είναι κάτω από το όριο
- Κόκκινο: και οι δύο δεξαμενές είναι κάτω από το όριο
"""

LOW_LEVEL = 20


def main() -> None:
    """Διαβάζει τα επίπεδα των δύο δεξαμενών από τον χρήστη και εκτυπώνει την κατάσταση τους."""

    # Data input
    tank1 = 60
    tank2 = 15

    # Processing: Έλεγχος επιπέδων δεξαμενών
    is_red_alarm = tank1 < LOW_LEVEL and tank2 < LOW_LEVEL
    is_orange_alarm = (tank1 < LOW_LEVEL) ^ (tank2 < LOW_LEVEL)  # XOR Bitwise operator

    # Εκτύπωση αποτελεσμάτων
    print(f"Δεξαμενή 1: {tank1}%, Δεξαμενή 2: {tank2}%")
    print(f"Κόκκινο: {is_red_alarm}")
    print(f"Πορτοκαλί: {is_orange_alarm}")


if __name__ == "__main__":
    main()