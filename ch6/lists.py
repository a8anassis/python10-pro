my_list = [1, 2, 3, 4, 5]
my_list2 = []
my_list12 = [0] * 3

lst_count = len(my_list)
count_3 = my_list.count(3)  # counts how many times 3 appears in the list

for i in range(len(my_list)):
    print(my_list[i])

for el in my_list:
    print(el)

for i, el in enumerate(my_list):
    print(f"Index: {i}, Element: {el}")

for el1, el2 in zip(my_list, my_list2):
    print(f"Element from my_list: {el1}, Element from my_list2: {el2}")

# add elements to the list
my_list.append(6)
my_list.extend([7, 8, 9])

# remove elements from the list
my_list.remove(3)
del my_list[0]  # remove the first element

# update elements in the list
my_list[0] = 10

# search for an element in the list
# Το in ελέγχει πρώτα is και μετά ==, άρα συμπεριφέρεται όπως το equals() της Java
if 4 in my_list:
    print("4 is in the list")

# search for an element in the list and get its index
if 4 in my_list:
    index = my_list.index(4)

# pythonic
try:
    index = my_list.index(4)
except ValueError:
    index = -1   # ή None, ή ό,τι σημαίνει «δε βρέθηκε»

# traverse in reverse the list and remove elements from the list
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] % 2 == 0:
        del my_list[i]

# traverse and remove elements from the list
my_list = [el for el in my_list if el % 2 != 0]     # list comprehension, creates a new list
my_list[:] = [el for el in my_list if el % 2 != 0]  # slice assignment, modifies the original list

# --- Slicing ---
lst = [10, 20, 30, 40, 50]
my_list3 = lst[1:3]      # [20, 30]
my_list4 = lst[:2]       # [10, 20]
my_list5 = lst[-2:]      # [40, 50]
my_list6 = lst[::2]      # [10, 30, 50]
my_list7 = lst[::-1]     # αντίστροφο αντίγραφο
