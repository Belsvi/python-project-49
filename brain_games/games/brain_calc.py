from random import choice, randint

from brain_games.scripts.engine import run_game


def calculation(num_1, num_2, operand):
    if operand == "+":
        return num_1 + num_2
    elif operand == '-':
        return num_1 - num_2
    elif operand == '*':
        return num_1 * num_2
    else:
        return ValueError(f'Unsupported {operand}')


def generate_question_and_answer():
    operands = ('+', '-', '*')
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operand = choice(operands)
    question = f'{num_1} {operand} {num_2}'
    correct_answer = calculation(num_1, num_2, operand)
    return question, correct_answer


def main():
    game_rule = 'What is the result of the expression?'
    run_game(generate_question_and_answer, game_rule, "Calculate Game")