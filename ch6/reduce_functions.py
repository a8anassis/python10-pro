"""Reduce functions: min(), max(), sum()."""


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# sum() function
sum_all = sum(x for x in nums)  # returns 55, generator expression
total = sum(x * x for x in nums if x % 2 == 0)  # returns 220, sum of squares of even numbers

# min() function
min_value = min(nums)  # returns 1
min_even = min(x for x in nums if x % 2 == 0)  # returns 2, minimum even number
min_length_name = min(names, key=len)  # returns "Bob", name with minimum length
min_length = min(len(w) for w in names)  # returns 3, length of the shortest name

# max() function
max_value = max(nums)  # returns 10
max_odd = max(x for x in nums if x % 2 != 0)  # returns 9, maximum odd number
max_length_name = max(names, key=len)  # returns "Charlie", name with maximum length
max_length = max(len(w) for w in names)  # returns 7, length of the longest name


# avg = sum(nums) / len(nums)  # returns 5.5, average of numbers
avg = sum(nums) / len(nums)  # returns 5.5, average of numbers

## all() function
all_even = all(x % 2 == 0 for x in nums)  # returns False, not all numbers are even
all_positive = all(x > 0 for x in nums)  # returns True, all numbers are positive


# any() function
any_even = any(x % 2 == 0 for x in nums)  # returns True, at least one number is even
any_negative = any(x < 0 for x in nums)  # returns False, no numbers are negative