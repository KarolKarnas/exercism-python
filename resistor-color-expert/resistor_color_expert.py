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

TOLERANCE_MAP = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10,
}

PREFIX_MAP = {'giga': 1000000000, 'mega': 1000000, 'kilo': 1000}


def resistor_label(colors):
    tolerance = ''
    prefix = ''
    ohms = 0
    if len(colors) == 4:
        ohms = (
            COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
        ) * 10 ** COLORS.index(colors[2])
        tolerance = f' ±{TOLERANCE_MAP[colors[-1]]}%'
    if len(colors) == 5:
        ohms = (
            COLORS.index(colors[0]) * 100
            + COLORS.index(colors[1]) * 10
            + COLORS.index(colors[2])
        ) * 10 ** COLORS.index(colors[3])
        tolerance = f' ±{TOLERANCE_MAP[colors[-1]]}%'

    for key, value in PREFIX_MAP.items():
        if ohms >= value:
            prefix = key
            ohms = ohms / value
            
    ohms = int(ohms) if ohms.is_integer() else round(ohms, 2)
    
    return f'{ohms} {prefix}ohms{tolerance}'
