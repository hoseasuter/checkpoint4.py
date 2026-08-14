import numpy as np
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))
marks = np.zeros((num_students, num_subjects), dtype=float)

student_names = []
for i in range(num_students):
    name = input(f"\nEnter the name of Student {i + 1}: ")
    student_names.append(name)
    for j in range(num_subjects):
        mark = float(input(f"  Enter marks for Subject {j + 1} (out of 100): "))
        marks[i, j] = mark


total_marks = np.sum(marks, axis=1)
percentage = (total_marks / (num_subjects * 100)) * 100
def get_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B+"
    elif pct >= 60:
        return "B"
    elif pct >= 50:
        return "C"
    else:
        return "F"
grades = [get_grade(p) for p in percentage]
print("\n" + "=" * 60)
print(f"{'Student Name':<20}{'Total Marks':<15}{'Percentage':<15}{'Grade':<10}")
print("=" * 60)
for i in range(num_students):
    print(f"{student_names[i]:<20}{int(total_marks[i]):<15}{percentage[i]:<15.2f}{grades[i]:<10}")
print("=" * 60)
