OPEN = ['[', '{', '(']
CLOSE = [']', '}', ')']


def is_paired(input_string):
    stack = []
    
    for char in input_string:
        if char in OPEN:
            open_index = OPEN.index(char)
            stack.append(CLOSE[open_index])
            print(1, stack)
        elif char in CLOSE:
            if len(stack) == 0 or stack.pop()!= char:
                return False 
            print(2, stack)
    return len(stack) == 0
