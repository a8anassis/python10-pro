"""Copy lists in Python."""

import copy

my_list = [1, 2, 3, 4, 5]

# Copy the list
copied_list = my_list   # safe copy, due to immutable nature of integers


matrix = [[1, 2], [3, 4], [5, 6]]

# deep copy of the matrix
deep_copied_matrix = copy.deepcopy(matrix)


# copy with slicing
sliced_list = my_list[:]  # shallow copy but safe copy, due to immutable nature of integers

