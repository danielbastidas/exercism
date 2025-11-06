def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = []
    reversed_binary_str = binary_str[::-1]
    for index, bit in enumerate(reversed_binary_str):
        if index == 4 and bit == '1':
            handshake.reverse()
        elif bit == '1':
            handshake.append(actions[index])
    return handshake
