from random import randint
from time import sleep

from prompt import string

from brain_games.cli import welcome_user
from brain_games.wrong_answer_output import wrong_answer_output


def is_even_game(name):
    sleep(1)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sleep(1)
    
    correct_guesses = 0

    while correct_guesses < 3:

        number = randint(1, 10000)
        answer = string(f'Question: {number}\nYour answer: ')
        correct_answer = 'no' if number % 2 else 'yes'

        if answer != correct_answer:
            wrong_answer_output(answer, correct_answer, name)

            return

        print('Correct!')
        sleep(1)

        correct_guesses += 1

    print(f'Congratulations, {name}!')

    return


def main():
    name = welcome_user()
    is_even_game(name)


if __name__ == "__main__":
    main()
