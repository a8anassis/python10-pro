"""Αλγόριθμοι με συναρτήσεις και προκλήσεις.

1. Armstrong Number. Ένας Armstrong number (ή narcissistic number) είναι ένας αριθμός
που ισούται με το άθροισμα των ψηφίων του, καθένα υψωμένο στη δύναμη του αριθμού των ψηφίων.
Για παράδειγμα, ο αριθμός 153 είναι ένας Armstrong number, επειδή 1^3 + 5^3 + 3^3 = 153.
"""


def is_armstrong_number(num: int) -> bool:
    """Ελέγχει αν ένας αριθμός είναι Armstrong number"""
    str_digits = str(num)
    num_digits = len(str_digits)
    return num == sum(int(digit) ** num_digits for digit in str_digits)


def swap_case(s: str) -> str:
    """Εναλλάσσει το case των χαρακτήρων σε ένα string.

    Με conditional expression, μπορούμε να ελέγξουμε αν ένας χαρακτήρας
    είναι κεφαλαίος ή πεζός και να τον μετατρέψουμε ανάλογα.
    Για παράδειγμα, το "Hello World" γίνεται "hELLO wORLD".
    """
    # return s.swapcase()
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)


def repeat_text(text: str, n: int) -> str:
    """Επαναλαμβάνει το κείμενο n φορές"""
    return text * n

# Έστω μία συνάρτηση count_chars_in_text(text: str, char: str, limit: int) -> int
# και η οποία μετράει πόσες φορές εμφανίζεται ένας χαρακτήρας σε ένα κείμενο μέχρι ένα όριο limit.
def count_chars_in_text(text: str, char: str, limit: int) -> int:
    """Μετράει πόσες φορές εμφανίζεται ένας χαρακτήρας σε ένα κείμενο μέχρι ένα όριο limit"""
    return text.count(char, 0, limit)   # limit excluded - limit - 1