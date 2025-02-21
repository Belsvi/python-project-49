from math import sqrt


def is_check(num):
    prime_num = sqrt(num)
    length = int(prime_num + 1)
    if num == 2 or num == 3:
        Flag = True
    for i in range(2, length):
        if num % i == 0:
            Flag = False
            break
        else:
            Flag = True
    return Flag

