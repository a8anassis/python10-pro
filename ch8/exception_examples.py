"""Exception Examples με χειρισμό εξαιρέσεων"""

grades = {"alice": 90, "bob": 85}
text = None

try:
    int("abc")  # Προσπάθεια μετατροπής μη έγκυρου string σε ακέραιο
except ValueError as e:
    print(f"Σφάλμα: {e}")

try:
    result = "coding" / 2  # Προσπάθεια διαίρεσης string με ακέραιο
except TypeError as e:
    print(f"Σφάλμα: {e}")

try:
    print(grades["charlie"])  # Προσπάθεια πρόσβασης σε μη υπάρχον κλειδί
except KeyError as e:
    print(f"Σφάλμα: {e}")

try:
    print(text.upper())  # Προσπάθεια κλήσης μεθόδου σε None
except AttributeError as e:
    print(f"Σφάλμα: {e}")

try:
    with open("non_existent_file.txt", encoding="utf-8") as file:  # Προσπάθεια ανοίγματος μη υπάρχοντος αρχείουυ
        content = file.read()
        print(content)
except OSError as e:
    print(f"Σφάλμα: {e}")