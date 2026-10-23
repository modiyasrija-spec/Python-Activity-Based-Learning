# Case Study 66: Student Academic Risk Classification

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    attendance = float(input("Enter attendance percentage: "))
    average_marks = float(input("Enter average marks: "))

    if attendance < 75 or average_marks < 40:
        risk = "High Risk"
    elif attendance < 85 or average_marks < 60:
        risk = "Moderate Risk"
    else:
        risk = "Low Risk"

    students.append((name, attendance, average_marks, risk))

print("\n===== STUDENT ACADEMIC RISK REPORT =====")

for student in students:
    name, attendance, average_marks, risk = student

    print("\nStudent:", name)
    print("Attendance:", attendance, "%")
    print("Average marks:", average_marks)
    print("Academic risk:", risk)