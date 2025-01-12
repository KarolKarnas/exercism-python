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

PREFIX_MAP = {'giga': 1000000000, 'mega': 1000000, 'kilo': 1000}


def label(colors):
    ohms = (
        COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
    ) * 10 ** COLORS.index(colors[2])


    prefix = ''
    for key, value in PREFIX_MAP.items():
        if ohms >= value:
            prefix = key
            ohms = int(ohms / value)

    return f'{ohms} {prefix}ohms'

