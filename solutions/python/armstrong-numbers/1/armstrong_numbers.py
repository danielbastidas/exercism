def is_armstrong_number(number):
    numberOfDigits = len(str(number))
    remainder = number
    sum = 0
    while (remainder > 0):
        digit = remainder % 10
        sum+=pow(digit, numberOfDigits)
        remainder = remainder // 10
    return sum == number