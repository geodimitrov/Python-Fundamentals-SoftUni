
n = int(input())

students_grades = {}

for _ in range(n):
    student = input()
    grade = float(input())
    
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

filtered_students = {}
for student, grades in students_grades.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        filtered_students[student] = avg_grade

for name, grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {grade:.2f}")

