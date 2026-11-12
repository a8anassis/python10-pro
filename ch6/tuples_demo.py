my_tuple = (1, 2, 3)
a, b, c = 2, 6, 9

# swap values of a and b
a, b = b, a

# traverse the tuple and print each value with for loop
for value in my_tuple:
    print(value)

print()

print(*my_tuple, sep=", ")  # unpack the tuple and print each value

num1 = my_tuple[0]
num2 = my_tuple[-1]     # returns the last value of the tuple

my_tuple_slice = my_tuple[1:3]  # returns a slice of the tuple (2, 3)
