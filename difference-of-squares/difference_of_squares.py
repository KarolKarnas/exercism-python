def square_of_sum(number):
    result = 0
    for num in range(1, number + 1):
        result += num
    return pow(result, 2)


def sum_of_squares(number):
    result = 0
    for num in range(1, number + 1):
        result += pow(num, 2)
    return result

def difference_of_squares(number):
    return square_of_sum(number=number) - sum_of_squares(number)
