import operator
from random import choice, randint
from time import sleep

from prompt import string

from brain_games.cli import welcome_user
from brain_games.wrong_answer_output import wrong_answer_output


def calc_game(name):

    ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    }

    sleep(1)
    print('What is the result of the expression?')
    sleep(1)

    correct_guesses = 0

    while correct_guesses < 3:
        num_1, num_2 = randint(0, 100), randint(1, 20)  
        oper = choice(('+', '-', '*'))

        answer = string(f'Question: {num_1} {oper} {num_2}\nYour answer: ')

        correct_answer = str(ops[oper](num_1, num_2))

        if answer != correct_answer:
            wrong_answer_output(answer, correct_answer, name)

            return

        print('Correct!\n')
        sleep(1)

        correct_guesses += 1

    print(f'Congratulations, {name}!\n')


def main():
    name = welcome_user()
    calc_game(name)


if __name__ == "__main__":
    main()