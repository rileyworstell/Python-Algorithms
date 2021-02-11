"""
You're given an array of integers where each integer represents a jump of its value in the array.
If a jump spills past the arrays bounds, it wraps over to the other side.
Write a functions that takes a bool representing whether the jumps in the array form a cycle and ends at starting index
"""


# O(n) Time & O(1) Space
def has_single_cycle(array):
    position = 0
    jump = array[0]
    for i in range(len(array)):
        j = position + jump
        while j < 0:
            j += len(array)
        while j >= len(array):
            j -= len(array)
        if array[j] == None:
            return False
        else:
            if i != len(array) - 1:
                jump = array[j]
                array[j] = None
                position = j
            else:
                if j == 0:
                    return True
                else:
                    return False


# array = [2, 3, 1, -4, -4, 2]
array = [1, -1, 1, -1]
print(has_single_cycle(array))
