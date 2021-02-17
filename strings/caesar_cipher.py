"""
Ceasar Chipher
"""


def caesarChipherEncryptor(string, key):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    string = [char for char in string]
    for i in range(len(string)):
        alphabet_index = letters.index(string[i]) + key
        while alphabet_index > 25:
            alphabet_index -= 26
        string[i] = letters[alphabet_index]
    string = ''.join(string)
    return string


string = 'xyz'
key = 2  # 'zab'
print(caesarChipherEncryptor(string, key))
