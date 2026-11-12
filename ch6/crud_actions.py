"""CRUD operations in lists"""


products = ["Milk", "Bread", "Eggs", "Cheese"]

# Traverse
for product in products:
    print(product, sep=" | ")

print()

# enumerate
for index, product in enumerate(products):
    print(f"{index}: {product}", sep=" | ")

# Insert at the end
products.append("Butter")
products.extend(["Yogurt", "Juice"])

# Insert at a specific index
products.insert(2, "Cereal")

# Update an element
products[1] = "Whole Grain Bread"   # IndexError: Αν το index είναι εκτός ορίων, θα προκύψει σφάλμα

# Delete an element by value
products.remove("Eggs")

# Delete with del statement
del products[0]  # IndexError: Αν το index είναι εκτός ορίων, θα προκύψει σφάλμα

# Search for an element
if "Cheese" in products:
    print("Cheese is available in the list.")

# safe search with try-except
try:
    index = products.index("Butter")
    product = products[index]       # IndexError: Αν το index είναι εκτός ορίων, θα προκύψει σφάλμα
    print(f"Butter is at index {index}.")
    products[index] = "Margarine"  # Update the product at the found index
    products.remove("Butter")
    print(f"Butter is at index {index}.")
except ValueError:
    print("Butter is not in the list.")
except IndexError:
    print("Index is out of range.")