def label(colors):
    giga = 1000000000
    mega = 1000000
    kilo = 1000
    resistor_band_dict = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    resistance_value = 0
    answer = ""
    
    for index, color in enumerate(colors[0:2]):
        resistance_value += resistor_band_dict[color]*10**(1-index)

    resistance_value *= 10**resistor_band_dict[colors[2]]

    if resistance_value > giga and resistance_value % giga == 0:
        answer = str(int(resistance_value / giga)) + " gigaohms"
    elif resistance_value > mega and resistance_value % mega == 0:
        answer = str(int(resistance_value / mega)) + " megaohms"
    elif resistance_value > kilo and resistance_value % kilo == 0:
        answer = str(int(resistance_value / kilo)) + " kiloohms"
    else:
        answer = str(resistance_value) + " ohms"
    
    return answer

print(label(["red", "black", "red"]))
