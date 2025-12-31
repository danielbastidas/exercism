def square_root(number):
    square_root = max(number - 1, 1)
    while square_root > 0:
        if square_root * square_root == number:
            break
        else:
            square_root = square_root - 1

    return square_root