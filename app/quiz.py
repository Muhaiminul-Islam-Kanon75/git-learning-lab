QUESTIONS = [
    {
        "question": "Which command creates a new Git repository?",
        "answer": "git init",
    },
    {
        "question": "Which command uploads local commits to GitHub?",
        "answer": "git push",
    }
]


def calculate_score(answers):
    return sum(1 for a in answers if a is True)


def start_quiz():
    score = 0

    for item in QUESTIONS:
        user_answer = input(f"{item['question']} ")

        if user_answer.strip() == item["answer"]:
            print("Correct")
            score += 1
        else:
            print(f"Wrong. Correct answer: {item['answer']}")

    print(f"Final Score: {score}/{len(QUESTIONS)}")