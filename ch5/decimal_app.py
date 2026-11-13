"""Ακρίβεια δεκαδικών με τη χρήση της βιβλιοθήκης decimal"""


from decimal import Decimal
from decimal import ROUND_HALF_UP

def main() -> None:
    # Ορισμός της ακρίβειας των δεκαδικών

    # Δημιουργία δεκαδικών αριθμών
    price = Decimal("19.99")
    tax_rate = Decimal("0.24")

    vat = price * tax_rate
    total_price = price + vat

    # Στρογγυλοποίηση του τελικού ποσού
    total_price = total_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Εκτύπωση των αποτελεσμάτων
    print(f"ΦΠΑ: {vat}")
    print(f"Συνολική τιμή: {total_price}")


if __name__ == "__main__":
    main()