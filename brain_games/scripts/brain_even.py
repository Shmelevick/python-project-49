from random import randint
from time import sleep

from prompt import string

from brain_games.cli import welcome_user


def is_even_game(name):
    sleep(1)
    print('Answer "yes" if the number is even, otherwise answer "no".\n')
    sleep(2)
    
    correct_guesses = 0
    
    while correct_guesses < 3:

        number = randint(1, 10000)
        answer = string(f'Question: {number}\nYour answer: ')
        correct_answer = 'no' if number % 2 else 'yes'

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!\n\n\n"
            )
            sleep(2)

            correct_guesses = 0

            continue

        print('Correct!\n')
        sleep(1)

        correct_guesses += 1

    print(f'Congratulations, {name}!\n')

    return


def main():
    name = welcome_user()
    is_even_game(name)


if __name__ == "__main__":
    main()
