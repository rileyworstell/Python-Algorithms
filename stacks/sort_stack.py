"""
Recursively sorts the stack in place.
"""


def sortStack(stack):
    if len(stack) == 0:
        return stack
    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack, top)
    return stack


def insertInSortedOrder(stack, value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)


stack = [-5, 2, -2, 4, 3, 1]
print(sortStack(stack))