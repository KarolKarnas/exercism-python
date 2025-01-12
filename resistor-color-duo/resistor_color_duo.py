COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def value(colors):
    result = ''
    for index in range(0,2):
        result += str(COLORS.index(colors[index]))
    return int(result)