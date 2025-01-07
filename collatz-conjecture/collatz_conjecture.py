def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    def ifEven(n):
        return n // 2

    def ifOdd(n):
        return 3 * n + 1

    steps = 0
    while number != 1:
        steps += 1
        if number % 2 == 0:
            number = ifEven(number)
        elif number % 2 != 0:
            number = ifOdd(number)
    return steps
