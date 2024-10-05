"""

the color.py file is used for display the color string on print function

myString = colors_string('red', 'SyntaxError...')
print(myString) -> print with color red

"""

# the all color code '\033'
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'grey': '\033[90m'
}


# pick the good element in colors dict and return this values
def colors_string(color_name, *value):
    value = " ".join(value)
    try:
        return colors[color_name] + value + '\033[0m'
    except:
        return value
