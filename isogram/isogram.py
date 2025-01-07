def is_isogram(string):
    lower_str = string.lower()
    for letter in lower_str:
        if letter.isalpha() and lower_str.count(letter) > 1:
            return False
    return True


# def is_isogram(string):
#     return all(string.lower().count(letter) == 1 for letter in string.lower() if letter.isalpha())