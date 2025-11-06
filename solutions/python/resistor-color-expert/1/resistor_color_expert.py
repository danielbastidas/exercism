def resistor_label(colors):
    band_values = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    tolerances = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5, 'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}

    if len(colors) == 1:
        return "0 ohms"

    resistance_value_str = ""
    resistance_value = 0
    tolerance = 0
    for index, color in enumerate(colors):
        if index == len(colors) - 2: # the previous to the last band
            resistance_value = int(resistance_value_str) * 10**band_values[color]
        elif index == len(colors) - 1: # the last band
            tolerance = tolerances[color]
        else: # the first bands
            resistance_value_str += str(band_values[color])

    response = ""
    if resistance_value >= 1000000:
        response = str(format_number(resistance_value / 1000000)) + " megaohms ±" + str(tolerance) + "%"
    elif resistance_value >= 1000:
        response = str(format_number(resistance_value / 1000)) + " kiloohms ±" + str(tolerance) + "%"
    else:
        response = str(format_number(resistance_value)) + " ohms ±" + str(tolerance) + "%"

    return response

def format_number(n):
    return f"{n:.0f}" if n == int(n) else f"{n}"