from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import is_even_game


def main():
    name = welcome_user()
    is_even_game(name)


if __name__ == "__main__":
    main()
