def main():
    print("===== GENERAL KNOWLEDGE QUIZ =====\n")

    score = 0

    question1 = "What is the capital of France? "
    answer1 = input(question1).strip().lower()
    if answer1 == "paris":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Paris.\n")

    question2 = "Which planet is known as the Red Planet? "
    answer2 = input(question2).strip().lower()
    if answer2 == "mars":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Mars.\n")

    question3 = "What is the formula for water? "
    answer3 = input(question3).strip().lower()
    if answer3 == "h2o":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is H2O.\n")

    print("===== QUIZ FINISHED =====")
    print(f"Your final score is: {score}/3")


if __name__ == "__main__":
    main()