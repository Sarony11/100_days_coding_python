"""List comprehension"""
numbers = [1,2,3]
square_numbers = [x**2 for x in numbers]
print(square_numbers)


new_list = [x*2 for x in range(1,6)]
print(new_list)

names = ["Alex", "Dave", "Saul", "Joshep", "Marian", "Tormur"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

"""Dict comprehension"""

import random
student_score = {
    "Alex": "",
    "Daniel": "",
    "Dave": "",
    "Marian": "",
    "Tormur": ""
}

new_score = { student: random.randint(1,100) for student in student_score }
print(new_score)
new_score2 = { name: score*2 for name, score in new_score.items() }
print(new_score2)
approved_students = { name: score for name, score in new_score2.items() if score > 60}
print(approved_students)