"""Χρήση του match-case για την επιλογή ενός είδους από το μενού."""

EXIT_CHOICE = "4"

def decide_on_choice(choice: str) -> str:
    """Επιστρέφει το είδος που επιλέχθηκε από το μενού."""
    match choice:
        case "1":
            return "Κατάθεση"
        case "2":
            return "Ανάληψη"
        case "3":
            return "Υπόλοιπο"
        case "4":
            return "Έξοδος"
        case _:
            return "Άγνωστη επιλογή"


def main() -> None:
    """Κύρια συνάρτηση για την εκτέλεση του προγράμματος."""
    while True:
        print("Μενού:")
        print("1. Κατάθεση")
        print("2. Ανάληψη")
        print("3. Υπόλοιπο")
        print("4. Έξοδος")

        choice = input("Επιλέξτε μια επιλογή (1-4): ")

        if choice == EXIT_CHOICE:
            print("Έξοδος από το πρόγραμμα.")
            break

        result = decide_on_choice(choice)

        print(f"Επιλέξατε: {result}")


if __name__ == "__main__":
    main()