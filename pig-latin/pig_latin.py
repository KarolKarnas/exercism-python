VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = [
    'b',
    'c',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l',
    'm',
    'n',
    'p',
    'q',
    'r',
    's',
    't',
    'v',
    'w',
    'x',
    'y',
    'z',
]

OTHER = ['xr', 'yt']


def move_consonant(text):
    if text[0] in CONSONANTS:
        return translate(text[1:] + text[0])


def translate(text):
    splitted = text.split()
    if len(splitted) > 1:
        translated_words = [translate(word) for word in splitted]
        result = ' '.join(translated_words)
        return result
    
    first_letter = text[0]
    first_two_letters = text[0:2]
    if first_letter in VOWELS or first_two_letters in OTHER:
        return f'{text}ay'

    if first_letter != 'y' and 'y' in text and first_letter in CONSONANTS:
        if len(text) == 2:
            return text[1:] + text[0] + 'ay'
        return move_consonant(text)

    if first_letter in CONSONANTS:
        if first_two_letters == 'qu':
            return translate(text[2:] + text[:2])
        return move_consonant(text)

    return first_two_letters


