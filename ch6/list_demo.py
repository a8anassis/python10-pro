my_list = [1, 2, 3]
my_list2 = [0] * 5      # Δημιουργεί μια λίστα με 5 μηδενικά, like repeat(0, 5) in other languages

# Εκτύπωση της λίστας με range
for i in range(len(my_list)):   # IndexError: Index out of range, because len(my_list) is 3, so range(4) gives indices 0, 1, 2, 3
    print(my_list[i])

# Εκτύπωση της λίστας, safe version without IndexError
for item in my_list:
    print(item)

num1 = my_list[1]
num2 = my_list[-1]  # last element of the list

print(*my_list, sep=", ")

my_slice = my_list[1:3]  # Δημιουργεί ένα slice της λίστας από index 1 έως 2 (το 3 είναι exclusive)





