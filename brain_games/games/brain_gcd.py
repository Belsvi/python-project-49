from random import randint

from brain_games.scripts.engine import run_game


def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return num_1 + num_2


def generate_question_and_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f'{num_1} {num_2}'
    correct_answer = str(gcd(num_1, num_2))
    return question, correct_answer


def main():
    game_rule = 'Find the greatest common divisor of given numbers.'
    run_game(generate_question_and_answer, game_rule, "Gcd Game")
