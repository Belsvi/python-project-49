from math import sqrt
from random import randint

from brain_games.scripts.engine import run_game


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = randint(1, 1000)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def main():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_question_and_answer, game_rule, "Prime Game")