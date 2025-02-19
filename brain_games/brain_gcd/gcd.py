import prompt
from brain_games.brain_calc.hello import hello_gcd
from brain_games.brain_gcd.data_gcd import input_data
from brain_games.brain_gcd.check import is_check


def is_gcd():
    name = hello_gcd()
    count = 0
    while count < 3:
        num_1, num_2 = input_data()
        print(f'Question: {num_1} {num_2}')
        answer = prompt.integer('Your answer: ')
        answer_check = is_check(num_1, num_2)
        if answer == answer_check:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;). Correct answer was '{answer_check}.'")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')