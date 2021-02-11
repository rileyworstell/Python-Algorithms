"""
Write a function that takes in an array of integers and returns a sorted version. 
Use selection sort.
"""


# O(n^2) Time & O(1) Space Worst case
def selection_sort(array):
    pointer = 0
    for j in range(len(array)):
        for i in range(len(array)):
            while i < pointer:
                i += 1
            if array[pointer] > array[i]:
                pointer = i
        array[j], array[pointer] = array[pointer], array[j]
        pointer = j + 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]

print(selection_sort(array))
