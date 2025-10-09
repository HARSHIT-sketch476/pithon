questions = {
"What does CPU stand for?": "central processing unit",
"What does GPU stand for?": "graphics processing unit",
"What does RAM stand for?": "random access memory",
"What does PSU stand for?": "power supply unit",
}

score = 0

print("Welcome to the Quiz Game!")
print("NOTE: Answers are case-insensitive.\n")

for question, correct_answer in questions.items():
  user_answer = input(f"{question} ").strip().lower()
if user_answer == correct_answer.lower():
  print("Correct! 🎉")
  score += 1
else:
  print(f"Incorrect! The correct answer is: {correct_answer}\n")

  print(f"\nYou got {score}/{len(questions)} questions correct!")
percentage = (score / len(questions)) * 100
print(f"Your score percentage is: {percentage:.2f}%")
