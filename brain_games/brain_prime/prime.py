import prompt
from brain_games.brain_calc.hello import hello_prime
from brain_games.brain_prime.data import input_data
from brain_games.brain_prime.check import is_check


def is_prime():
    name = hello_prime()
    count = 0
    while count < 3:
        num = input_data()
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        Flag = is_check(num)
        if (answer == 'yes' and Flag is True) or (answer == 'no' and Flag is False):
            print('Correct!')
            count += 1
        if answer == 'yes' and Flag is False:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        if answer == 'no' and Flag is True:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        if answer != 'yes' and Flag is True:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was 'yes'.'")
            print(f"Let's try again, {name}!")
            break
        if answer != 'no' and Flag is False:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')