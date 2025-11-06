def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    answer = ''
    factors = []
    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            factors.append(i)

    aliquotSum = sum(factors)

    if aliquotSum == number:
        answer = "perfect"
    elif aliquotSum > number:
        answer = "abundant"
    else:
        answer = "deficient"

    return answer
        
