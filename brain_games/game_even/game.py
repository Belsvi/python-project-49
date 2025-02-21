from random import randint
from brain_games.game_even.hello import say_hello
import prompt


def even_game():
    name = say_hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        num = randint(0, 100)
        print(f'Question: {num}')
        answer = prompt.string('You answer: ')
        if (num % 2 == 0 and answer == 'yes') or (num % 2 != 0 and answer == 'no'):
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        else:
            if num % 2 == 0 and (answer == 'no' or answer != 'yes'):
                print(f"'{answer}' is wrong answer ;(."
                      f"Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
            else:
                print(f"'{answer}' is wrong answer ;(."
                      f" Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
            break