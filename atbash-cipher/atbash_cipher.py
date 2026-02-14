ALPHA = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text: str):
    result =''
    splitted = list(plain_text.lower())
    counter = 0
    for ch in splitted:
        if ch == ' ' or ch in ',.':
            continue
        if counter == 5:
            result += ' '
            counter = 0
        if ch.isdigit():
            result += ch
            counter += 1
        if ch in ALPHA:
            counter += 1
            i = ALPHA.index(ch)
            result += CIPHER[i]
   
    return result


def decode(ciphered_text):
    result = ''
    splitted = list(ciphered_text.lower())
    for ch in splitted:
        if ch == ' ':
            continue
        if ch.isdigit():
            result += ch
        if ch in CIPHER:
            i = CIPHER.index(ch)
            result += ALPHA[i]
   
    return result
