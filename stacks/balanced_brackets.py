"""
A string is balanced if each bracket has a closing bracket.
"""


def balancedBrackets(string):
    brackets = ' () {} [] '
    stack = []
    for i in range(len(string)):
        if string[i] in brackets:
            if len(stack) > 0 and string[i] == brackets[brackets.index(stack[-1])+1]:
                stack.pop()
            else:
                stack.append(string[i])
    if len(stack) > 0:
        return False
    else:
        return True


string = '([])(){}(())()()'

print(balancedBrackets(string))
