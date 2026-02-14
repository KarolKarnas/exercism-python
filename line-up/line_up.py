def line_up(name, number):
    last = number % 10
    last_two = number % 100

    suffix = 'th'
    if last == 1 and last_two != 11:
        suffix = 'st'
    elif last == 2 and last_two != 12:
        suffix = 'nd'
    elif last == 3 and last_two != 13:
        suffix = 'rd'

    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'
