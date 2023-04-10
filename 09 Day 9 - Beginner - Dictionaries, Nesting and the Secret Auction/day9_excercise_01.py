"""
In this excercise we learn:
- How to manipulate and create dictionaries.
"""
"""
Scoring Criteria
Score 100-91 -> Outstanding
Score 90-81 -> Exceeded Expectations
Score 80-71 -> Acceptable
Score 70 or less -> Fail
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student_name in student_scores:
    if student_scores[student_name] >= 91:
        student_grades[student_name] = "Outstanding"
    elif student_scores[student_name] >= 81:
        student_grades[student_name] = "Exceeded Expectations"
    elif student_scores[student_name] >= 71:
        student_grades[student_name] = "Acceptable"
    else: student_grades[student_name] = "Fail"

print(student_grades)