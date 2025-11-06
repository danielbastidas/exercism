def is_valid(isbn):

    isbn = isbn.replace('-','')
    if len(isbn) != 10:
        return False
    
    sum = 0
    all_valid_digits = True

    for index in range(10, 0, -1):

        if not is_valid_digit(isbn[-index], index):
            all_valid_digits = False
            break
            
        if index == 1:
            if isbn[-index] == 'X':
               sum += 10 * index
            else:
                sum += int(isbn[10 - index]) * index
        else:
            sum += int(isbn[10 - index]) * index

    return all_valid_digits and sum % 11 == 0

def is_valid_digit(digit, index):
    return (ord(digit) >= 48 and ord(digit) <= 57) or (digit == 'X' and index == 1)