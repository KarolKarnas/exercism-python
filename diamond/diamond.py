import string


def rows(letter):
    alf = string.ascii_uppercase
    num_alf = alf.find(letter) + 1
    a = 2 * num_alf - 1
    result = []
    for i in list(range(num_alf - 1)) + list(range(num_alf - 1, -1, -1)):
        print(i)
        my_letter = alf[i]
        dots_number = num_alf - i - 1
        dots = dots_number * " "
        first = dots + my_letter + dots
        other_dots_side_number = dots_number
        other_dots_middle = a - 2 - (2 * other_dots_side_number)
        other_row = (
            other_dots_side_number * " "
            + my_letter
            + other_dots_middle * " "
            + my_letter
            + other_dots_side_number * " "
        )
        if i == 0:
            result.append(first)
        else:
            result.append(other_row)
    return result
