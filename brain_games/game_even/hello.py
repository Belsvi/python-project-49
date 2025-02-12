import prompt


def say_hello():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return  name