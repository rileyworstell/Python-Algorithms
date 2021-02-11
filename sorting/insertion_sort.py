"""
Write a function that takes in an array of integers and returns a sorted version. 
Use insertion sort.
"""


# O(n^2) Time & O(1) Space Worst case but Best case O(n) Time (if its already sorted)
def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]

print(insertion_sort(array))
