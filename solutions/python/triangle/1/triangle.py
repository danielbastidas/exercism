def is_valid(sides):
    a, b, c = sides
    has_zeroes = a == 0 or b == 0 or c == 0
    return not has_zeroes and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    a, b, c = sides
    return is_valid(sides) and a == b and b == c


def isosceles(sides):
    a, b, c = sides
    return is_valid(sides) and (a == b or b == c or a == c)


def scalene(sides):
    return is_valid(sides) and not equilateral(sides) and not isosceles(sides)
