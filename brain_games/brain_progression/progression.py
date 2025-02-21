import prompt

from brain_games.brain_calc.hello import hello_progression
from brain_games.brain_progression.data_progression import input_data


def is_progression():
    name = hello_progression()
    count = 0
    while count < 3:
        progression, missing_number = input_data()
        print(f'Question: {progression}')
        answer = prompt.integer('Your answer: ')
        if answer == int(missing_number):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{missing_number}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')