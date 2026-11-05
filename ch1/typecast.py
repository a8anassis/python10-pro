"""Type casting demonstration."""

num1 = int("32")                    # string to int
num2 = float("3.14")                # string to float
str_num = str(100)                  # int to string
truncated_num = int(3.99)           # float to int (truncates decimal part)!!! απώλεια πληροφορίας
num3 = int("abc")                    # ValueError: invalid literal for int() with base 10: 'abc'

# result1 = "Coding" + 7              # TypeError: can only concatenate str (not "int") to str
result2 = "Coding" + str(7)         # Correct way to concatenate string and int
result3 = 5 + 3.2                   # int + float results in float

# Μετατροπές με bool()
# Ψευδή θεωρούνται τα εξής: 0, 0.0, "", [], {}, None
bool1 = bool(0)                     # 0 → False
bool2 = bool(1)                     # 1 → True
bool3 = bool("Hello")               # non-empty string → True
bool4 = bool("")                    # empty string → False

print("Num1 is:" + str(num1))
print(f"Num1 is: {num1}")