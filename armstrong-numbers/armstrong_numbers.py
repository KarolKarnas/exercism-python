from functools import reduce


def is_armstrong_number(number):
    power = len(str(number))
    digits = [int(digit) for digit in str(number)]
    sum = reduce(lambda acc, digit: acc + digit**power, digits, 0)
    return sum == number