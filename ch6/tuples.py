my_tuple = (1, 2, 3, 4, 5)
empty_tuple = ()
single = (5,)        # προσοχή: χρειάζεται κόμμα· το (5) είναι απλώς int
also_tuple = 1, 2, 3 # οι παρενθέσεις είναι προαιρετικές, το κόμμα φτιάχνει το tuple

for i in range(len(my_tuple)):
    print(my_tuple[i])

for el in my_tuple:
    print(el)

for i, el in enumerate(my_tuple):
    print(i, el)

# add elements → δεν υπάρχει append/extend, φτιάχνουμε ΝΕΟ tuple
my_tuple = my_tuple + (6,)
my_tuple = my_tuple + (7, 8, 9)
my_tuple += (10,)    # επίσης νέο tuple + rebinding, όχι in-place


# search for an element in the tuple
# Το in ελέγχει πρώτα is και μετά ==, όπως και στις λίστες
if 4 in my_tuple:
    print("4 is in the tuple")

# pythonic
try:
    index = my_tuple.index(4)
except ValueError:
    index = -1

count = my_tuple.count(4)   # επιστρέφει πόσες φορές εμφανίζεται το 4
# index() και count() είναι οι ΜΟΝΕΣ μέθοδοι του tuple

# reverse traversal (ανάγνωση μόνο)
for i in range(len(my_tuple) - 1, -1, -1):
    print(my_tuple[i])

for el in reversed(my_tuple):
    print(el)

# filtering → πάντα νέο tuple (δεν υπάρχει αντίστοιχο του [:] =)
my_tuple = tuple(el for el in my_tuple if el % 2 != 0)  # generator expression → tuple()
# (el for el in ...) σκέτο ΔΕΝ είναι "tuple comprehension", είναι generator

# --- Slicing --- (ίδιο με λίστες, επιστρέφει tuple)
tpl = (10, 20, 30, 40, 50)
my_tuple3 = tpl[1:3]     # (20, 30)
my_tuple4 = tpl[:2]      # (10, 20)
my_tuple5 = tpl[-2:]     # (40, 50)
my_tuple6 = tpl[::2]     # (10, 30, 50)
my_tuple7 = tpl[::-1]    # αντίστροφο αντίγραφο

# --- Packing / Unpacking --- (η βασική χρήση των tuples)
point = (3, 4)
x, y = point
first, *rest = (1, 2, 3, 4)      # first=1, rest=[2, 3, 4]  ← το rest είναι list!
a, b = 1, 2
a, b = b, a                      # swap χωρίς temp

def min_max(seq):
    return min(seq), max(seq)    # επιστροφή πολλών τιμών = tuple
lo, hi = min_max([3, 1, 7])

# --- Συναρτήσεις / τελεστές ---
len(tpl), min(tpl), max(tpl), sum(tpl)
sorted(tpl)                      # επιστρέφει LIST, όχι tuple
my_tuple1 = (0,) * 3                         # (0, 0, 0)
