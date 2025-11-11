scores = [
    ('Alice', 80),
    ('Bob', 90),
    ('Alice', 85),
    ('Charlie', 100),
    ('Bob', 95)
]

student_scores = {}

for name,score in scores:
    if name in student_scores:
        student_scores[name].append(score)
    else:
        student_scores[name] = [score]

print(student_scores)
