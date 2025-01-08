def is_valid(isbn: str):
    new_str = isbn.replace('-', '')[::-1]
    if len(new_str) != 10:
        return False
    total = 0
    for index, number in enumerate(new_str):
        if index == 0 and number == 'X':
            number = '10'
        if not number.isdigit():
            return False
        total += int(number) * (index + 1)
    return total % 11 == 0
