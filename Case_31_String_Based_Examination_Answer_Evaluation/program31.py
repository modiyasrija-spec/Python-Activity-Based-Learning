# Case Study 31: String-Based Examination Answer Evaluation

questions = [
    "What is the capital of India?",
    "Which language are we learning?",
    "What does CPU stand for?"
]

correct_answers = [
    "New Delhi",
    "Python",
    "Central Processing Unit"
]

n = len(questions)
student_answers = []
score = 0

print("===== EXAMINATION ANSWER EVALUATION =====")

for i in range(n):
    print("\nQuestion", i + 1, ":", questions[i])
    answer = input("Enter your answer: ").strip().lower()
    student_answers.append(answer)

    if answer == correct_answers[i].strip().lower():
        score += 1

print("\n===== RESULT =====")

for i in range(n):
    print("Question", i + 1, ":", questions[i])
    print("Your answer:", student_answers[i])
    print("Correct answer:", correct_answers[i])

    if student_answers[i] == correct_answers[i].strip().lower():
        print("Result: Correct")
    else:
        print("Result: Incorrect")

print("\nTotal questions:", n)
print("Correct answers:", score)
print("Incorrect answers:", n - score)
print("Final score:", score, "/", n)