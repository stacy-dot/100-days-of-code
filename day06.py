quiz = {
    "What is the capital of Kenya?": "nairobi",
    "What does CPU stand for?": "central processing unit",
    "Which language is this quiz written in?": "python",
    "Who is the founder of Microsoft?": "bill gates"
}
answer1 = input("What is the capital of Kenya? ").lower()
answer2 = input("What does CPU stand for? ").lower()
answer3 = input("Who is the founder of Microsoft? ").lower()

score = 0

if answer1 == "nairobi":
    score += 1

if answer2 == "central processing unit":
    score += 1

if answer3 == "bill gates":
    score += 1

print(f"\nYou got {score} out of 3 correct!")
