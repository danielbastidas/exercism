def value(colors):
    band_colors_map = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    bands_value = 0
    
    for index, color in enumerate(colors):
        if index < 2:
            bands_value += (10/pow(10, index)) * band_colors_map[color] 
        else:
            break

    return bands_value
