from random import choice, randint


def input_data():
    result = []
    first_item = randint(1, 100)
    difference = randint(1, 10)
    amount = 10
    for i in range(amount):
        progression = first_item + (i * difference)
        result.append(progression)
    for i in range(len(result)):
        result[i] = str(result[i])
    missing_number = choice(result)
    for i in range(len(result)):
        if result[i] == missing_number:
            result[i] = '..'
        progression_correct = ' '.join(result)
    return progression_correct, missing_number