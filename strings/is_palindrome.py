"""
A string is a palindrome if it is written the same forwards as it is backwards.
Write a function to return if a string is a palindrome or not (bool).
"""


def is_palindrome(string):
    l_pointer = 0
    r_pointer = len(string) - 1
    while l_pointer <= r_pointer:
        if string[l_pointer] == string[r_pointer]:
            l_pointer += 1
            r_pointer -= 1
        else:
            return False
    return True


string = 'abcdajcba'
print(is_palindrome(string))
