"""List comprehensions in Python

Create new lists from an existing list using list comprehensions.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# map
doubled_nums = [x * 2 for x in nums]
str_nums = [str(x) for x in nums]

clean_and_lower_names = [name.strip().lower() for name in names]

# Filtering
even_nums = [x for x in nums if x % 2 == 0]

# Multiple conditions for filtering
even_nums_gt_5 = [x for x in nums if x % 2 == 0 and x > 5]

# if / else in list comprehension, mapping values to "even" or "odd"
even_odd = ["even" if x % 2 == 0 else "odd" for x in nums]

# flattening a matrix
flattened_matrix = [num for row in matrix for num in row]


# Αντίστοιχα και για άλλες δομές δεδομένων, όπως sets, dictionaries και tuples, μπορούμε να χρησιμοποιήσουμε comprehensions για να δημιουργήσουμε νέα sets, dictionaries ή tuples από υπάρχουσες δομές δεδομένων.
squares_set = {x ** 2 for x in nums}        # set comprehension, duplicates will be removed
squared_dict = {x: x ** 2 for x in nums}    # dictionary comprehension
lazy = (x * x for x in nums)                #  generator expression, lazy evaluation, χωρίς λίστα στη μνήμη



