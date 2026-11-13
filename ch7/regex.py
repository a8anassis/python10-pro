"""Κανονικές εκφράσεις (Regular Expressions)"""

import re

text = """Πρώτη συνάντηση: 01-01-2026 και 2η συνάντηση: 31-11-2026 ."""

# Όλα τα matches που ταιριάζουν με την ημερομηνία
pattern = r"\d{2}-\d{2}-\d{4}"
matches = re.findall(pattern, text)
print(f"Βρέθηκαν οι ημερομηνίες: {matches}")

# Όλα τα matches με groups
pattern = r"(\d{2})-(\d{2})-(\d{4})"
matches = re.findall(pattern, text)
for day, month, year in matches:            # επιστρέφει μια λίστα από tuples [(day, month, year), ...]
    print(f"Ημέρα: {day}, Μήνας: {month}, Έτος: {year}")


# fullmatch - validates the entire string
date = "01-01-2026"
if re.fullmatch(pattern, date):
    print(f"{date} είναι έγκυρη ημερομηνία")

# fullmatch - validates the entire string
date = "01-01-2026"
match = re.fullmatch(pattern, date) is not None
print(f"{'Έγκυρο' if match else 'Μη έγκυρο'}: {date}")


# Strong password validation
STRONG_PASSWORD_REGEX = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
for pwd in ["Password123!", "weakpass", "StrongPass1@", "NoSpecialChar1", "Short1!"]:
    ok = STRONG_PASSWORD_REGEX.fullmatch(pwd) is not None
    print(f"{'Έγκυρος' if ok else 'Μη έγκυρος'} κωδικός: {pwd}")






