import prompt

NUMBER_OF_GAMES = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question_answer(question):
    print(question)
    answer = prompt.string('Your answer: ')
    return answer


def compare_answer(answer, result):
    return str(answer).strip().lower() == str(result).strip().lower()
