"""
Write a function that takes in a string of words and returns the words reversed.
"""


# O(n) Time & O(n) Space
def reverse_words(string):
    result = ''
    pointer = len(string) - 1
    end_of_word = pointer
    while pointer >= 0:
        if string[pointer] == ' ':
            result += string[pointer + 1:end_of_word+1] + ' '
            end_of_word = pointer - 1
            pointer -= 1
        elif pointer == 0:
            result += string[pointer:end_of_word+1]
            pointer -= 1
        elif string[pointer] != ' ':
            pointer -= 1
    return result


string = 'Something is the best!'
print(reverse_words(string))
