def wrong_answer_output(answer, correct_answer, name):
    
    if answer != correct_answer:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.\n"
            f"Let's try again, {name}!\n\n\n"
        )

    return