from random import choice, randint
from time import sleep

from prompt import string

from brain_games.cli import welcome_user
from brain_games.wrong_answer_output import wrong_answer_output


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def prime_generator(num):
    prime_n = num

    while not is_prime(prime_n):
        prime_n += 1

    return prime_n


def is_prime_game(name):
    sleep(1)
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    sleep(1)

    correct_guesses = 0

    while correct_guesses < 3:

        number = randint(1, 500)
        prime_number = prime_generator(number)
        guessed_number = choice((number, prime_number))

        answer = string(f'Question: {guessed_number}\nYour answer: ')
        correct_answer = 'yes' if is_prime(guessed_number) else 'no'

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
    is_prime_game(name)


if __name__ == "__main__":
    main()