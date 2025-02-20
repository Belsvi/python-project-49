from brain_games.brain_calc.hello import hello_prime
from brain_games.brain_prime.data import input_data
import prompt


def is_prime():
    name = hello_prime()
    count = 0
    while count < 3:
        num = input_data()
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if (num == 2 and answer == 'yes') or (num % 2 != 0 and answer == 'yes') or (num % 2 == 0 and answer == 'no'):
            print('Correct!')
            count += 1
            if count == 3:
                print(f"Congratulations, {name}!")
        else:
            if num % 2 == 0 and answer == 'yes':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
            if (num == 2 and answer != 'yes') or (num % 2 != 0 and answer != 'yes'):
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
            if num % 2 == 0 and answer != 'no':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break