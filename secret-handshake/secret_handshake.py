ACTION = ['wink', 'double blink', 'close your eyes', 'jump', 'reverse']

def commands(binary_str):
    result = []
    for index, sign in enumerate(binary_str[::-1]):
        if sign == '1':
            if index == 4:
                return result[::-1]
            result.append(ACTION[index])
    return result
