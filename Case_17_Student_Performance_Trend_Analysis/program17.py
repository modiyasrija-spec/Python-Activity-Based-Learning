n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = float(input(f"Enter marks for test {j + 1}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    if marks[2] > marks[0]:
        trend = "Improving"
    elif marks[2] < marks[0]:
        trend = "Declining"
    else:
        trend = "Stable"

    students.append((name, marks, average, trend))

print("\n===== STUDENT PERFORMANCE REPORT =====")

for student in students:
    name, marks, average, trend = student

    print("\nStudent:", name)
    print("Test marks:", marks)
    print(f"Average marks: {average:.2f}")
    print("Performance trend:", trend)