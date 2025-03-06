def distance(strand_a, strand_b):
    splited_a = list(strand_a)
    splited_b = list(strand_b)
    hamming = 0
    if len(splited_a) != len(splited_b):
        raise ValueError("Strands must be of equal length.")
    for index, sign in enumerate(splited_a):
        if sign != splited_b[index]:
            hamming += 1
    return hamming
