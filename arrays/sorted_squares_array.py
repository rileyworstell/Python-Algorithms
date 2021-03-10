"""
Function that takes in non-empty array of integers that are sorted and returns a new array of the same length with the squares sorted.
"""


# O(nlog(n)) Time & O(n) Space
# def sortedSquaredArray(array):
#     for i in range(len(array)):
#         array[i] = array[i] ** 2
#     array.sort()
#     return array


# O(n) Time * O(n) Space
def sortedSquaredArray(array):
    arr = [0 for _ in array]
    pointer_1 = 0
    pointer_2 = len(array) - 1
    pointer_arr = len(array) - 1
    while pointer_arr >= 0:
        if abs(array[pointer_1]) > abs(array[pointer_2]):
            arr[pointer_arr] = array[pointer_1] ** 2
            pointer_1 += 1
        else:
            arr[pointer_arr] = array[pointer_2] ** 2
            pointer_2 -= 1
        pointer_arr -= 1
    return arr


array = [-5, -1, 0, 1, 5]
print(sortedSquaredArray(array))
