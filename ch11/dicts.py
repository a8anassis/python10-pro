"""Dictionary examples"""


empty_dict = {}
grades = {"alice": 90, "bob": 85, "charlie": 92}

alice_grade = grades["alice"]  # Πρόσβαση σε τιμή με βάση το κλειδί

# upserting: αν το κλειδί υπάρχει ήδη, η τιμή του αντικαθίσταται με τη νέα τιμή
grades.update({"david": 88 , "bob": 90})

del grades["charlie"]  # Διαγραφή κλειδιού και τιμής

# iterating over keys and values
for student, grade in grades.items():
    print(f"{student}: {grade}")

# iterating with keys only
for student in grades.keys():
    print(f"Student: {student}")

# iterating with values only
for grade in grades.values():
    print(f"Grade: {grade}")


students = {"alice": 90, "bob": 45, "charlie": 92}

passed = { name: grade for name, grade in students.items() if grade >= 50 }

