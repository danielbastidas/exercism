bands = [("black", 0), ("brown", 1), ("red", 2), ("orange", 3), ("yellow", 4), ("green", 5), ("blue", 6), ("violet", 7), ("grey", 8), ("white", 9)]

def color_code(color):    
    for band_color, code in bands:
        if band_color == color:
            return code

def colors():
    band_colors = []
    for color, _ in bands:
        band_colors.append(color)

    return band_colors