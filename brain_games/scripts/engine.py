from brain_games.scripts.input_data import (
    NUMBER_OF_GAMES,
    ask_question_answer,
    compare_answer,
    welcome_user,
)


def run_game(game_logic, game_rule, game_name):
    name = welcome_user()
    print(game_rule)
    round_counter = 0

    while round_counter < NUMBER_OF_GAMES:
        question, correct_answer = game_logic()
        answer = ask_question_answer(f'Question: {question}')
        right_answer = compare_answer(answer=answer, result=correct_answer)

        if right_answer:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

