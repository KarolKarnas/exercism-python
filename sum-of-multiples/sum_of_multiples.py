def sum_of_multiples(limit, multiples):
    result = set()
    for multiple in multiples:
        if multiple == 0: continue
        for num in range(1, limit):
            if num % multiple == 0:
                result.add(num)

    return sum(result)
