"""Slicing lists in Python"""

# sorted by grades
students = ["Άννα", "Βασίλης", "Γιώργος", "Δημήτρης", "Ελένη", "Ζωή", "Ηλίας", "Θεοδώρα"]

#top 3 students
top3 = students[:3]         # ["Άννα", "Βασίλης", "Γιώργος"]
bottom3 = students[-3:]     # ["Ζωή", "Ηλίας", "Θεοδώρα"]
middle2 = students[3:5]         # ["Δημήτρης", "Ελένη"]

# reverse the list
reversed_students = students[::-1]  # ["Θεοδώρα", "Ηλίας", "Ζωή", "Ελένη", "Δημήτρης", "Γιώργος", "Βασίλης", "Άννα"]

print(*reversed_students, sep=", ")




