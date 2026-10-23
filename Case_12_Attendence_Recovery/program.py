total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes <= 0:
    print("Invalid total classes")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid number of classes attended")
else:
    percentage = attended_classes / total_classes * 100
    print(f"Current attendance: {percentage:.2f}%")

    if percentage >= 75:
        print("Attendance requirement satisfied")
    else:
        required = 0
        while (attended_classes + required) / (total_classes + required) * 100 < 75:
            required += 1
        print("Additional consecutive classes required:", required)