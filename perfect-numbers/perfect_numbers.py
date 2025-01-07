from enum import Enum


class Aliquot(Enum):
    PERFECT = 'perfect'
    ABUNDANT = 'abundant'
    DEFICIENT = 'deficient'


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquots = []

    for number_x in range(1, number):
        if number % number_x == 0:
            aliquots.append(number_x)

    aliquots_sum = sum(aliquots)

    if aliquots_sum == number:
        return Aliquot.PERFECT.value
    if aliquots_sum > number:
        return Aliquot.ABUNDANT.value
    if aliquots_sum < number:
        return Aliquot.DEFICIENT.value
    return
