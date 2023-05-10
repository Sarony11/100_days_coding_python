student_dict = {
    "students": ["Angela", "Saul", "Lily"],
    "score": [56,76,98]
}

import pandas
student_df = pandas.DataFrame(student_dict)
print(student_dict)

for (index,row) in student_df.iterrows():
    print(index)

for (index,row) in student_df.iterrows():
    print(row)

for (index,row) in student_df.iterrows():
    print(row.students)