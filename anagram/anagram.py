def find_anagrams(word, candidates):
    result = []
    for candidate in candidates:
        if candidate.lower() != word.lower() and "".join(
            sorted(word.lower())
        ) == "".join(sorted(candidate.lower())):
            result.append(candidate)

    return result
