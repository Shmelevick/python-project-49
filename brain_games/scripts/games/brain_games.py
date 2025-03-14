from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_calc import calc_game
from brain_games.scripts.games.brain_even import is_even_game
from brain_games.scripts.games.brain_gcd import gcd_game
from brain_games.scripts.games.brain_progression import progression_game
from brain_games.scripts.games.brain_prime import is_prime_game


def main():
    name = welcome_user()
    is_even_game(name)
    calc_game(name)
    gcd_game(name)
    progression_game(name)
    is_prime_game(name)



if __name__ == "__main__":
    main()
