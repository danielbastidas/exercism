def reverse(text):
    reverse_str = ''
    for index in range(len(text)-1, -1, -1):
        reverse_str += text[index]
    return reverse_str
        
