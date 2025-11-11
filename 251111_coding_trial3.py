students = [
    {'id': 101, 'name': 'Alice', 'score': 85},
    {'id': 102, 'name': 'Bob', 'score': 92},
    {'id': 103, 'name': 'Charlie', 'score': 78},
    {'id': 104, 'name': 'David', 'score': 95}
]

high_scorers = []

for student in students:
    if student['score']>90:
        high_scorers.append(student)

student_names = []
for student in students:
    student_names.append(student['name'])

