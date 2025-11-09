def square_of_sum(number):
    return pow((number * (number + 1)) / 2, 2)

def sum_of_squares(number):
    sum = 0
    for iter_number in range(number + 1):
        sum = sum + pow(iter_number, 2)
    return sum

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
