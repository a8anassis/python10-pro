"""Ανάληψη από ATM."""

EXIT_VALUE = 0
BANKNOTE = 20
INITIAL_BALANCE = 1000


def main() -> None:
    """Εκτελεί αναλήψεις ελέγχοντας πρώτα τα error states."""
    balance = INITIAL_BALANCE

    while True:
        print(f"Το υπόλοιπό σας είναι: {balance}€")
        amount = int(input("Εισάγετε το ποσό που θέλετε να αναλάβετε (0 για έξοδο): "))

        if amount == EXIT_VALUE:
            print("Έξοδος από το πρόγραμμα.")
            break

        if amount < 0:
            print("Σφάλμα: Το ποσό δεν μπορεί να είναι αρνητικό.")
            continue

        if amount > balance:
            print("Σφάλμα: Δεν έχετε αρκετά χρήματα στο λογαριασμό σας.")
            continue

        if amount % BANKNOTE != 0:
            print(f"Σφάλμα: Το ποσό πρέπει να είναι πολλαπλάσιο των {BANKNOTE}\u20AC.")
            continue

        balance -= amount
        print(f"Η ανάληψη των {amount}\u20AC ολοκληρώθηκε. Το νέο υπόλοιπο είναι: {balance}\u20AC\n")


if __name__ == "__main__":
    main()
