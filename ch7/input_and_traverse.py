"""Είσοδος str και traverse με for loop."""

def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""

    # Είσοδος δεδομένων
    name = input("Εισάγετε το όνομά σας: ")

    # Εκτύπωση χαρακτήρων με for loop
    print("Οι χαρακτήρες του ονόματός σας είναι:")
    for char in name:
        print(char, end=" ")

if __name__ == "__main__":
    main()