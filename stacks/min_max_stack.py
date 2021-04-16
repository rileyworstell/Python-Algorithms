"""
Write a MinMaxStack class for a Min Max Stack.
Pushing and Popping values, and peeking at the top.
Also, should keep track of the min and max values.
"""


class MinMaxStack:
    def __init__(self, values=[]):
        self.values = []
        self.minMaxStack = []

    def peek(self):
        return self.values[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.values.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack)-1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.values.append(number)

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]


stack = MinMaxStack()
stack.push(5)
stack.push(5)
stack.push(5)
stack.push(5)
stack.push(5)
stack.push(8)
stack.push(8)
stack.push(0)
stack.push(8)
stack.push(9)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
