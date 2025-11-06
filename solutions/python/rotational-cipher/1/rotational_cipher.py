def rotate(text, key):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    ciphered = ""
    for letter in text:
        if letter.isalpha():
            index = alphabet.index(letter.lower())
            if letter.isupper():
                ciphered += alphabet[(index + key) % 26].upper()
            else:
                ciphered += alphabet[(index + key) % 26]
        else:
            ciphered += letter

    return ciphered