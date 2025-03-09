def append(list1, list2):
    return list1 + [item for item in list2]


def concat(lists):
    result = []
    for item in lists:
        result += item
    return result


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    result = 0
    for _ in list:
        result += 1
    return result


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        result = function(initial, item)
        return foldl(function, list[1:], result)
    return initial


def foldr(function, list, initial):
    if list != []:
        result = function(initial, list[-1])
        return foldr(function, list[:-1], result)
    return initial


def reverse(list):
    result = []
    start = 1
    for _ in list:
        result += [list[-(start)]]
        start += 1
    return result


