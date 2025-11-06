def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    collatz = number
    while (collatz != 1):
        collatz = collatz // 2 if collatz % 2 == 0 else 3 * collatz + 1
        steps+=1
    return steps
        
