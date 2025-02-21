from random import choice, randint


def input_data():
    num_1 = randint(0, 50)
    num_2 = randint(0, 50)
    operators = ('+', '-', '*')
    operator = choice(operators)
    if operator == '+':
        num = num_1 + num_2
    elif operator == '-':
        num = num_1 - num_2
    elif operator == '*':
        num = num_1 * num_2
    return num_1, num_2, operator, num