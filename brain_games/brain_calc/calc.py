import prompt
from brain_games.brain_calc.hello import hello_calc
from brain_games.brain_calc.data import input_data


def is_calc():
    name = hello_calc()
    count = 0
    while count < 3:
        num_1, num_2, operator, num = input_data()
        print(f'Question: {num_1} {operator} {num_2}')
        answer = prompt.integer('Your answer: ')
        if answer == num:
            print('Correct!')
            count += 1
        if answer != num:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{num}'.")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')