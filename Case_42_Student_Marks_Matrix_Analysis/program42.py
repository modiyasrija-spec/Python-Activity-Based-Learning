# Case Study 42: Student Marks Matrix Analysis

rows = int(input("Enter number of students: "))
cols = int(input("Enter number of subjects: "))

if rows <= 0 or cols <= 0:
    print("Invalid number of students or subjects")
else:
    marks_matrix = []

    for i in range(rows):
        student_marks = []
        print("\nStudent", i + 1)

        for j in range(cols):
            mark = float(input(f"Enter marks for subject {j + 1}: "))
            student_marks.append(mark)

        marks_matrix.append(student_marks)

    print("\n===== STUDENT MARKS MATRIX =====")

    for i in range(rows):
        print("Student", i + 1, ":", marks_matrix[i])
        total = sum(marks_matrix[i])
        average = total / cols
        print("Total marks:", total)
        print(f"Average marks: {average:.2f}")

    print("\n===== SUBJECT-WISE AVERAGES =====")

    for j in range(cols):
        subject_total = 0

        for i in range(rows):
            subject_total += marks_matrix[i][j]

        subject_average = subject_total / rows
        print(f"Subject {j + 1} average: {subject_average:.2f}")