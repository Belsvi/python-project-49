from random import randint

from brain_games.scripts.engine import run_game


def generate_progression(first_item, step, length):
    progression = []
    for i in range(length):
        progression.append(first_item + (i * step))
    return progression


def generate_question_and_answer():
    length = 10
    first_item = randint(1, 100)
    step = randint(1, 10)
    progression = generate_progression(first_item, step, length)

    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    progression_str = ' '.join(map(str, progression))
    question = progression_str
    return question, correct_answer


def main():
    game_rule = 'What number is missing in the progression?'
    run_game(generate_question_and_answer, game_rule, "Progression Game")
