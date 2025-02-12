import prompt


def hello_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    return name

def answer():
    answer = prompt.integer('Answer:')
    print(type(answer))
    if answer == str(answer):
        print('wrong')
    print(answer)