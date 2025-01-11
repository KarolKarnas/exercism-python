alpha = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text, key):
    result = ''
    is_upper = False
    for sign in text:
        if sign.isupper():
            is_upper = True
            
        index = alpha.find(sign.lower())
        if index != -1:
            rot_index = index + key
            if rot_index >= 26:
                rot_index = rot_index - 26
            if is_upper:        
                result += alpha[rot_index].upper()
                is_upper = False
            else:
                result += alpha[rot_index]
                
        if index == -1:
            result += sign
                        
    return result
