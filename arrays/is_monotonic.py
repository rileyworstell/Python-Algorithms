"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing 
"""


# O(n) Time & O(1) Space
def is_monotonic(array):
    if (len(array) == 1) or (len(array) == 0):
        return True
    is_increasing = 2
    for i in range(len(array) - 1):
        if (array[i] < array[i+1]):
            if ((is_increasing != True) and (is_increasing != 2)):
                return False
            elif (is_increasing == 2):
                is_increasing = True
        elif (array[i] > array[i+1]):
            if ((is_increasing != False) and (is_increasing != 2)):
                return False
            elif (is_increasing == 2):
                is_increasing = False
    return True


array = [1, 2]
print(is_monotonic(array))
