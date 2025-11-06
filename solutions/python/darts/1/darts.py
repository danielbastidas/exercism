import math

def score(x, y):
    score = 0
    if is_inside_circle(x, y, 1): # inner circle
        score = 10
    elif is_inside_circle(x, y, 5): # middle circle
        score = 5
    elif is_inside_circle(x, y, 10): # outer circle
        score = 1
    return score

def is_inside_circle(x, y, radius):
    # hypotenuse formula to check if the distance between the center and the point is inside the radius of the circle
    return math.sqrt(pow(abs(x), 2) + pow(abs(y), 2)) <= radius