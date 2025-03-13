from random import randint
from time import sleep

from prompt import string

from brain_games.cli import welcome_user
from brain_games.wrong_answer_output import wrong_answer_output


def get_gcd(a, b):
    while b:

        a, b = b, a % b

    return a


def gcd_game(name):
    sleep(1)
    print('Find the greatest common divisor of given numbers.\n')
    sleep(1)

    correct_guesses = 0

    while correct_guesses < 3:
        common_divisor = randint(3, 10)

        num_1 = randint(1, 10) * common_divisor
        num_2 = randint(1, 10) * common_divisor
        while num_2 == num_1:
            num_2 = randint(1, 10) * common_divisor

        answer = string(f'Question: {num_1} {num_2}\nYour answer: ')

        correct_answer = str(get_gcd(num_1, num_2))

        if answer != correct_answer:
            wrong_answer_output(answer, correct_answer, name)

            sleep(2)

            continue

        print('Correct!\n')
        sleep(1)

        correct_guesses += 1

    print(f'Congratulations, {name}!\n')

    return


def main():
    name = welcome_user()
    gcd_game(name)


if __name__ == "__main__":
    main()