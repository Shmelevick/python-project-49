from random import randint
from time import sleep

from prompt import string

from brain_games.cli import welcome_user
from brain_games.wrong_answer_output import wrong_answer_output


def progression_game(name):
    sleep(1)
    print('What number is missing in the progression?\n')
    sleep(1)

    correct_guesses = 0

    while correct_guesses < 3:
        first_num = randint(2, 20)
        step = randint(2, 20)
        row = [num for num in range(first_num, first_num + 10 * step, step)]

        rand_index = randint(1, 9)

        correct_answer = str(row[rand_index])
        row[rand_index] = '..'

        answer = string(f'Question: {" ".join(map(str, row))}\nYour answer: ')

        if answer != correct_answer:
            wrong_answer_output(answer, correct_answer, name)

            return

        print('Correct!\n')
        sleep(1)

        correct_guesses += 1

    print(f'Congratulations, {name}!\n')

    return


def main():
    name = welcome_user()
    progression_game(name)


if __name__ == "__main__":
    main()